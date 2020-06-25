from clitv import configuration
import asyncio
import logging

logging.basicConfig(filename='clitv.log')

def search(terms, sources=configuration.sources()):
    results = asyncio.run(search_many_sources(terms, sources))
    flatten = lambda l: [item for sublist in l for item in sublist]
    return flatten([format_search_result(r) for r in results])

def format_search_result(result):
    source = result[0]
    result = result[1].decode("utf-8")
    result = result.split("\n")
    #Remove the last newline
    result.pop()
    if len(result) % 4 != 0:
        raise Exception("Search command failed", str(result))
    acc = []
    while len(result) > 0:
        head = result[:4]
        logging.error(head)
        acc.append({'id': head[0],
                    'source': source,
                    'title': head[1],
                    'author': head[2],
                    'desc': head[3]
                   })
        result = result[4:]
    return acc

async def search_many_sources(terms, sources):
    results = []
    for k, v in sources.items():
        results.append(await search_one_source(terms, k, v))
    return results

async def search_one_source(terms, source_name, source_cmd):
    terms = "\"" + terms + "\""
    command_ = source_cmd["search"].split()
    command = []
    for e in command_:
        if e == "%s":
            command.append(terms)
        else:
            command.append(e)
    spawn = asyncio.create_subprocess_exec(command[0],
                                           *command[1:],
                                           stdout=asyncio.subprocess.PIPE)
    process = await spawn
    stdout, stderr = await process.communicate()
    return (source_name, stdout)
