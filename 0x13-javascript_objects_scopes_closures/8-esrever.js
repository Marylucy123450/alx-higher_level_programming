#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0; i < Math.floor(list.length / 2); i++) {
    const temp = list[i];
    list[i] = list[list.length - 1 - i];
    list[list.length - 1 - i] = temp;
  }
  return list;
};
