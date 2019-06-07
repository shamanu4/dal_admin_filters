// pduey: a couple of public and private functions to add or remove a query string parameter + value pair.
//
// I like this implementation because it transforms the query string into a coherent hash with unique keys
// and an Array for the values, so it handles repeated query string parameter names, which are meant to be
// interpreted as Arrays, yo. The "private" functions could, of course, be handy for other uses.
//
// The function names include "search" because they are derived from window.location.search.
// Ideally, I'd attach these to the window object, as in, window.location.prototype.
//

// pduey: add a variable/value pair to the current query string and return updated href

function search_replace(name, value) {
    var new_search_hash = search_to_hash();
    new_search_hash[decodeURIComponent(name)] = [];
    new_search_hash[decodeURIComponent(name)].push(decodeURIComponent(value));
    return hash_to_search(new_search_hash);
}

function search_add(name, value) {
    var new_search_hash = search_to_hash();
    if (!(decodeURIComponent(name) in new_search_hash)) {
        new_search_hash[decodeURIComponent(name)] = [];
    }
    new_search_hash[decodeURIComponent(name)].push(decodeURIComponent(value));
    return hash_to_search(new_search_hash);
}

// pduey: remove a variable/value pair from the current query string and return updated href
function search_remove(name, value) {
    var new_search_hash = search_to_hash();
    if (new_search_hash[name].indexOf(value) >= 0) {
        new_search_hash[name].splice(new_search_hash[name].indexOf(value), 1);
        if (new_search_hash[name].length == 0) {
            delete new_search_hash[name];
        }
    }
    return hash_to_search(new_search_hash);
}

function search_to_hash() {
    var h = {};
    if (window.location.search == undefined || window.location.search.length < 1) {
        return h;
    }
    q = window.location.search.slice(1).split('&');
    for (var i = 0; i < q.length; i++) {
        var key_val = q[i].split('=');
        // replace '+' (alt space) char explicitly since decode does not
        var hkey = decodeURIComponent(key_val[0]).replace(/\+/g, ' ');
        var hval = decodeURIComponent(key_val[1]).replace(/\+/g, ' ');
        if (h[hkey] == undefined) {
            h[hkey] = [];
        }
        h[hkey].push(hval);
    }
    return h;
}

function hash_to_search(h) {
    var search = String("?");
    for (var k in h) {
        for (var i = 0; i < h[k].length; i++) {
            search += search == "?" ? "" : "&";
            search += encodeURIComponent(k) + "=" + encodeURIComponent(h[k][i]);
        }
    }
    return search;
}
