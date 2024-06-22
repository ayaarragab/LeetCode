/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  if(s.length != t.length)
    return false;
  myMap_one = {};
  myMap_two = {};
  for(let i = 0; i < s.length; i++)
  {
    myMap_one[s[i]] = (myMap_one[s[i]] ||  0) + 1;
    myMap_two[t[i]] = (myMap_two[t[i]] ||  0) + 1;
  }
  for(let key in myMap_one)
  {
    if (myMap_one[key] !== myMap_two[key])
        return false
  }
  return true
};