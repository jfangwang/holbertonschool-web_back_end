// return an object on success and error object on failure

function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
export default loadBalancer;
