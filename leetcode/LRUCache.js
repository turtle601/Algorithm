// leetcode 146. LRUCache

/**
 * @param {number} capacity
 */
 var LRUCache = function(capacity) {
    this.capacity = capacity
    this.map = new Map();
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    // map에 key가 있다면 
    if (this.map.has(key)){
        // 우선순위 설정을 위해 삭제 후 다시 설정
        const val = this.map.get(key);
        this.map.delete(key);
        this.map.set(key,val);
        return val;
    // 없다면 return -1
    } else {
        return -1;
    }
    
    
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (this.get(key) === -1){
        if (this.map.size === this.capacity){
            for (let [firstKey] of this.map){
                this.map.delete(firstKey);
                break;
            }
        }
    }
    this.map.set(key, value);
};


