// return an object on success and error object on failure

function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (error) {
    queue.push(error.toString());
  }
  queue.push('Guardrail was processed')
  return queue;
}
export default guardrail;
