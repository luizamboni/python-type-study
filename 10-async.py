import asyncio
from typing import Awaitable, Coroutine, List

async def mock_query(n: int) -> str:
    print(f'chamada: {n}')

    await asyncio.sleep(n)
    return f'resultado da api chamada: {n}'

async def main() -> None:
    result: str
    exec: Awaitable[str]
    result = await mock_query(1)
    print(result)

    exec = mock_query(2)
    result = await exec
    print(result)

#    tasks: List[Coroutine[int,None, str]] = [ mock_query(n) for n in reversed(range(1, 11)) ]
#    or using Awaitble
    tasks: List[Awaitable[str]] = [ mock_query(n) for n in reversed(range(1, 11)) ]

    print(tasks)
    done, _ = await asyncio.wait(tasks, timeout=10.0, return_when='ALL_COMPLETED')

    print([task.result() for task in done])


    return


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

