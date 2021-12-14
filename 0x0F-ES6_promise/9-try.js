// return an object on success and error object on failure

function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction(), 'Guardrail was prcessed');
  } catch (error) {
    queue.push(`Error: ${error.toString()}`, 'Guardrail was processed');
  }
  return queue;
}
export default guardrail;
