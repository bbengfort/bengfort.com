/**
 *  debug.js
 *  Copyright (C) 2013 Bengfort.com
 *  For license information see LICENSE.txt
 *
 *  Creator: Benjamin Bengfort <benjamin@bengfort.com>
 *  Orgin:   Sat Sep 14 16:25:13 2013 -0400
 *
 *  Debugger helper scripts for AJAX functionality
 */

{% if debug %}
var DEBUG = true;
{% else %}
var DEBUG = false;
{% endif %}

function test_debug() {
    if (DEBUG) {
        console.log("The debug script is active!");
    } else {
        console.log("Debug mode isn't on, but the script is loaded.");
    }
}
