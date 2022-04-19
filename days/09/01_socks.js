// Concepts about DISCRETE MATHEMATICS
// https://en.wikipedia.org/wiki/Pigeonhole_principle

// function maximumDraws(n) {
//   // Write your code here

//   // Constraints
//   if (n < 0 && n < 10e6) {
//     return
//   }

//   // const div = Math.ceil(n / 2)
//   // const isQuoEven = div % 2 === 0
//   // const isQuo1 = div === 1 && div % 2 === 1

//   // // 2 = 3
//   // if(isQuo1) {
//   //   return n + 1
//   // }

//   // return isQuoEven ? n + 1 : n

//   let mx = 0
//   while(n--) {
//     mx++
//   }

//   return mx
// }

function maximumDraws(n) {
  // Constraints
  if (n < 0 && n < 10e6) {
    return
  }
  return n + 1
}

console.log(maximumDraws(1))
console.log(maximumDraws(2))

// Input
console.log(maximumDraws(751)) // 902490
console.log(maximumDraws(902489)) // 902489 - 902187 = 302
console.log(maximumDraws(902186)) // 935367 - 902186 = 33.181
console.log(maximumDraws(935366)) // 104022
console.log(maximumDraws(104021)) // 352949
console.log(maximumDraws(352948)) // 957846
console.log(maximumDraws(957845)) // 284779
console.log(maximumDraws(284778)) // 532796
