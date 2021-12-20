// Implement a function updateUniqueItems that returns an updated
// map for all items with initial quantity at 1
export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw Error('Cannot process');
  }
  map.forEach((val, key) => {
    if (val === 1) map.set(key, 100);
  });
  return (map);
}
