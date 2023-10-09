export default function cleanSet(set, startString) {
  if (!startString) return '';
  return [...set].filter((item) => item.startsWith(startString))
    .map((item) => item.replace(startString, '')).join('-');
}
