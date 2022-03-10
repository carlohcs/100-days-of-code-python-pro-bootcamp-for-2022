function lowestTriangle(trianglebase, area) {
  const triangleHeight = (a, b) => Math.round((2 * a) / b) // 2 * (a / b)
  const triangleArea = (h, b) => Math.round((h * b) / 2) // ( h * b ) / 2
  const isTriangle = (a, b) => {
    let triHeight = triangleHeight(a, b)
    let triArea = triangleArea(triHeight, b)

    return triHeight * 2 === triArea
  }

  let lowest = triangleHeight(area, trianglebase)

  // Constraints
  if (trianglebase <= 1 || trianglebase >= 10e6 || area <= 1 || area >= 10e6) {
    return
  }

  if (!isTriangle(area, trianglebase)) {
    while(trianglebase > 1 && area > 1) {
      if(isTriangle(area, trianglebase)){
        let calcHeight = triangleHeight(area, trianglebase)
        
        if(calcHeight < lowest) {
          lowest = calcHeight
        }
        
      }

      trianglebase--
      area--
    }
  }

  return lowest
}

console.log(lowestTriangle(4, 6)) // right: 3
console.log(lowestTriangle(17, 100)) // right: 12
console.log(lowestTriangle(327454, 885497)) // right: 6
