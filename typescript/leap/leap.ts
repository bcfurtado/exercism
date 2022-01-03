export function isLeap(year: number) {
  const isDivisibleBy4 = year % 4 === 0;
  const isDivisibleBy100 = year % 100 === 0;
  const isDivisibleBy400 = year % 400 === 0;

  if (isDivisibleBy4 && isDivisibleBy100) {
    return isDivisibleBy400;
  }

  return isDivisibleBy4;
}
