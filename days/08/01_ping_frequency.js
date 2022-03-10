// PING FREQUENCY
// WORKING!

function getStamps(times, freq = "minute", start = 0, end = 0) {
  times = times.sort()

  const FREQUENCIES = {
    MINUTE: 60,
    HOUR: 60 * 60,
    DAY: 60 * 60 * 24
  }
  const time = FREQUENCIES[freq.toLocaleUpperCase()]
  const qtdChunks = Math.ceil((end - start) / time)
  let chunks = []
  let chunksIndex = []

  let counter = 0
  let lastStart = start
  
  while (counter <= qtdChunks - 1) {
    lastTime = counter === qtdChunks - 1 ? end : lastStart + time - 1
    chunks[counter] = [lastStart, lastTime]
    counter++

    lastStart += time
  }

  chunks.forEach((chunk, index) => chunksIndex[index] = 0)

  for(let i = 0; i < times.length; i++) {
    for(let j = 0; j < chunks.length; j++) {
      let currentTime = times[i]
      let currentChunk = chunks[j]
      if(currentTime >= currentChunk[0] && currentTime <= currentChunk[1]) {
        chunksIndex[j]++
      }
    }
  }

  return chunksIndex
}

console.log(getStamps([5, 90, 110], "minute", 0, 150)) // RIGHT: [1, 2, 0] -> RETURNED: [1, 2, 0]

console.log(getStamps([100, 120, 170, 3600, 3800], "hour", 10, 4000)) // RIGHT: [4, 1] -> RETURNED: [4, 1]
