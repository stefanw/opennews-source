/*
Component: Search toggle
*/
(function( $ ) {

    "use strict";

    var componentName = "search-toggle",
        closeSelectors = "." + componentName + " .icon-close",
        pageClass = "page",
        panelClass = "site-search",
        openClass = "is-" + panelClass + "-open",
        transitioningClass = "is-transitioning",
        enhancedAttr = "data-enhanced-" + componentName,
        initSelector = "." + componentName + ":not([" + enhancedAttr + "])";

    $.fn[ componentName ] = function() {

        return this.each( function() {

            var $searchToggle = $( this ),
                sHref = $searchToggle.attr( "href" ),
                $searchPanel = $( sHref ),
                $body = $( "body" ),
                closeStr = '<span class="icon icon-close" href="#">Close</span>';

            if ( $searchPanel ) {
                $( ".header-main .search-toggle" ).append( closeStr );

                $( "." + panelClass ).on( "expand", function() {
                    $body.addClass( openClass );

                    if ( $( ".site-nav" ).is( ".collapsible-expanded" ) ) {
                        $( ".site-nav .collapsible-header" ).trigger( "click" );
                    }
                } );

                $( "." + panelClass ).on( "collapse", function() {
                    $body.removeClass( openClass );
                } );

                // Close the panel on (throttled) resize
                $( window ).on( "resize", SRC.utils.debounce( function() {
                    if ( $( "." + panelClass ).is( ".collapsible-expanded" ) ) {
                        $( "." + panelClass + " .collapsible-header" ).trigger( "click" );
                    }
                }, 250 ) );
            }

        });

    };

    // auto-init on enhance (which is called on domready)
    $( document ).on( "enhance", function( e ){
        var $sel = $( e.target ).is( initSelector ) ? $( e.target ) : $( initSelector, e.target );
        $sel[ componentName ]().attr( enhancedAttr, "true" );
    });

}( jQuery ));
