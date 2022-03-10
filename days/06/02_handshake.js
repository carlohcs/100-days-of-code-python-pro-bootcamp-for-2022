"use strict"

// const fs = require("fs")

// process.stdin.resume()
// process.stdin.setEncoding("utf-8")

// let inputString = ""
// let currentLine = 0

// process.stdin.on("data", function (inputStdin) {
//   inputString += inputStdin
// })

// process.stdin.on("end", function () {
//   inputString = inputString.split("\n")

//   main()
// })

// function readLine() {
//   return inputString[currentLine++]
// }

/*
 * Complete the 'handshake' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER n as parameter.
 */
// function handshake(n) {
//   let shakes = 0
//   let people = []

//   if (n < 0 || n >= 10e6) {
//     return
//   }

//   // Isso é lento
//   for (let index = 0; index < n; index++) {
//     people.push([])
//   }

//   // [
//   //   [], => 0
//   //   [], => 1
//   //   [] => 2
//   // ]

//   for (let i = 0; i < n; i++) {
//     let person = people[i]

//     for (let j = 0; j < n; j++) {
//       let personToGreet = people[j]

//       if(person === personToGreet) {
//         continue
//       }

//       // isso é lento
//       if (!person.some((element) => element == j)) {
//         person.push(j)
//         personToGreet.push(i)
//         shakes++
//       }
//     }

//     delete people[i]
//   }

//   return shakes
// }

// https://www.hackerrank.com/challenges/handshake/forum
// Try this reasoning:

// I (PersonA) am one out of N people, so I need to shake hands with (N-1) people. This reasoning holds true for all of the N people, so the number of hand shakes is N * (N-1). Now that PersonA and PersonB shook hands, PersonB and PersonA (same people, but from PersonB's perspective) don't need to shake anymore. So we initially counted each combination twice. Therefore, the number of hand shakes is

// nShakes = (N * (N-1)) / 2
function handshake(n) {
  if (n < 0 || n >= 10e6) {
    return
  }

  return (n * (n - 1)) / 2
}

const ns = [666, 4646, 3453, 3379, 1949, 6084, 3726, 1578, 1382, 1753]

ns.forEach((n) => console.log(handshake(n), "\n"))

// function main() {
//   const ws = fs.createWriteStream("./output.txt")

//   const t = parseInt(readLine().trim(), 10)

//   for (let tItr = 0; tItr < t; tItr++) {
//     const n = parseInt(readLine().trim(), 10)

//     const result = handshake(n)

//     ws.write(result + "\n")
//   }

//   ws.end()
// }
