/**
 *  helpers.js
 *  Copyright (C) 2013 Bengfort.com
 *  For license information see LICENSE.txt
 *
 *  Creator: Benjamin Bengfort <benjamin@bengfort.com>
 *  Orgin:   Sat Sep 14 16:33:27 2013 -0400
 *
 *  Helper functions that should be loaded on all pages.
 */

jQuery.noConflict();
(function($) {
    $(document).ready(function() {

        // On `ESC` got to admin site
        $(document).keyup(function(e) {
            if (e.keyCode == 27) {
                window.location = "/admin";
            }
        });

    });
})(jQuery);
