export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString === '') return '';
  
  return [...set].filter((item) => item.startsWith(startString))
    .map((item) => item.substring(startString.length)).join('-');
}
