// PING FREQUENCY

// On any website we make a request to the "ping" endpoint with the user credentials. 
// We want to analyse the number of requests per user to this endpoint in select periods of time. 
// These periods are partitioned into smaller chunks based on a certain frequency (minute/hour/day).

// For example, the period [10-3800] (in seconds) would be partitioned into the following time chunks with these frequencies:
// Minute (60 second chunks): [10-69], [70-129].....[3790-3800]
// Hour (60*60 second chunks): [10-3609], [3610-3800]
// Day (60*60*24 second chunks): [10-3800]

// You have to design and implement the following API:
// Class: PingFrequency
// Function: void recordPing(<string> userId, <integer> Time)
// Function: List<Integer> getUserPingsPerFrequency(<string> userId, <string> freq, <integer> startTime, <integer> endTime)

// Example:

// [user_id, timestamp(seconds)] 
// """
// ["user_1", 5]
// ["user_2", 15]
// ["user_2", 20]
// ["user_1", 90]
// ["user_3", 100]
// ["user_1", 110]
// ["user_3", 120]
// ["user_3", 170]
// ["user_2", 2500]
// ["user_3", 3600]
// ["user_3", 3800]

// User 1
// // ["user_1", 5]
// // ["user_1", 90]
// // ["user_1", 110]

// User 2
// ["user_2", 15]
// ["user_2", 20]

// user 3
// ["user_3", 100]
// ["user_3", 120]
// ["user_3", 170]
// ["user_3", 3600]
// ["user_3", 3800]

// INPUT - getUserPingsPerFrequency("user_1", "minute", 0, 150) // 150 / 60 = 2,5
// OUTPUT - [1, 2, 0]
// Explanation: This is partitioned into [0-59, 60-119, 120-150] 
// => Within the 0-59 window, the user pinged once, 
// and within the 60-119 window, the user pinged twice in that window. 
// They made no request in the last window, leading to final result of: [1, 2, 0]

// INPUT - getUserPingsPerFrequency("user_3", "hour", 10, 4000)
// OUTPUT - [4, 1]
// Explanation: This is partitioned into [10-3609, 3610-4000] 
// => Within the 10-3609 window, the user pinged 4 times, 
// and within the 3610-400 window, they made pinged once, 
// leading to the final result of: [4, 1]

// ABOVE A WRONG IMPLEMENTATION
function getStamps(times, freq = "minute", start = 0, end = 0) {

  console.log('FREQ IS: ', freq)

  let sumTimes = times.reduce((previous, current) => previous + current, 0)
  
  let finalFrequencies = []

  let reachedChunkLimit = 0

  const LIMITS = {
    MINUTE: 60,
    HOUR: 60 * 60,
    DAY: 60 * 60 * 24
  }
  let chunkLimit = LIMITS[freq.toLocaleUpperCase()]

  let currentChunkLimit = 0

  console.log('RUNNING FROM: ', start, ' TO ', end)
  for (let index = start; index <= end; index++) {
    if(currentChunkLimit === chunkLimit - 1) { // 60 - 1 = 59 / 120 - 1 = 119 ...
      console.log('CHUNK: ', index, ' TO ', chunkLimit - 1)
      finalFrequencies[reachedChunkLimit] = 1 + reachedChunkLimit
      reachedChunkLimit++

      sumTimes -= chunkLimit

      chunkLimit += LIMITS[freq.toLocaleUpperCase()]
    }

    currentChunkLimit++
  }

  return finalFrequencies
}

console.log(getStamps([5, 90, 110], 'minute', 0, 150)) // RIGHT: [1, 2, 0] -> RETURNED: [1, 2]

console.log(getStamps([100, 120, 170, 3600, 3800], 'hour', 10, 4000)) // RIGHT: [4, 1] -> RETURNED: [1]