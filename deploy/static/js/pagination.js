/*
 * Universal AJAX pagination script for ViUR
 * -----------------------------------------
 *
 * This script serves a universal pagination script to be used by ViUR, which uses JQuery to
 * access DOM elements. The script evolved from a view customer projects we performed and will
 * be extended, enhanced and improved from time to time.
 */

// Pagination for Lists
var allcursors = [];
var activerequest = false;

$(document).ready( function()
	{
		if( ! $(".js-listcursor:last").length )
			return;

		$(window).scroll( function()
		{
			var cursortag = $(".js-listcursor:last");
			var cursor = cursortag.data( "cursor" );

			if( activerequest || allcursors.indexOf( cursor ) >= 0 )
				return;

			activerequest = true;
			$(".js-loader").fadeIn();

			var params = {}, hash, url, i;
			var hashes = window.location.href.slice( window.location.href.indexOf( "?" ) + 1 ).split( "&" );

			if( cursortag.data( "module" ) )
				url = "/" + cursortag.data( "module" ) + "/list";
			else
			{
				var pos;

				if( (pos = window.location.href.indexOf("?")) >= 0 )
					url = window.location.href.substr(0, pos);
				else
					url = window.location.href;

				url = url.replace("view", "list");
			}

			for( i = 0; i < hashes.length; i++ )
			{
				hash = hashes[i].split("=");

				if( hash.length == 2 )
					params[ hash[0] ] = hash[1];
			}

			var param;
			for( i = 0; ( param = cursortag.data( "param" + i ) ); i++ )
				params[ param.substr( 0, param.indexOf("=") ) ] = param.substr( param.indexOf("=") + 1 );

			if( cursor )
				params[ "cursor" ] = cursor;

			params[ "style" ] = "next";

			console.log( "Calling >%s<", url );
			console.log( params );

			$.post( url, params, function( content )
			{
				var parent = cursortag.parent();

				if( parent.find(".js-insertmarker").length )
					$(content).insertBefore( parent.find(".js-insertmarker") );
				else
					parent.append( content );

				allcursors.push( cursor );

				$(".js-loader").fadeOut();
				activerequest = false;
			});
		});
	});
