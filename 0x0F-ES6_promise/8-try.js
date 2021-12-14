// return an object on success and error object on failure

function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw Error('cannot divide by 0');
  } else {
    return (numerator / denominator);
  }
}
export default divideFunction;
