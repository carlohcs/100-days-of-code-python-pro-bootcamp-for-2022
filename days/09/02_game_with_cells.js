// rows, columns
// https://www.hackerrank.com/challenges/game-with-cells/forum
function gameWithCells(n, m) {
  // Write your code here

  // Constraints
  if (n < 0 || m < 0 || n > 1000 || m > 1000) {
    return
  }

  // return Math.ceil((n * m) / (2 + 2))
  return Math.ceil(n / 2) * Math.ceil(m / 2)
  // return ( n * m ) / mdc
}

console.log(gameWithCells(2, 3)) // 2
console.log(gameWithCells(2, 2)) // 1
console.log(gameWithCells(1, 4)) // 2
console.log(gameWithCells(999, 1000)) // 250000
console.log(gameWithCells(39, 169)) // 1700

// 2 * 3 = 6 / 6 / 3 = 2

// 1 , 4

// | -- | -- | -- |
//      X    x
