
/**
 *	Vanilla Javascript library: Graph
 *
 *	Copyright 2013 Sung-ihk Yang (unikys at gmail.com)
 *
 *	Permission is hereby granted, free of charge, to any person obtaining a copy
 *	of this software and associated documentation files (the "Software"), to 
 *	deal in the Software without restriction, including without limitation the
 *	rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
 *	sell copies of the Software, and to permit persons to whom the Software is
 *	furnished to do so, subject to the following conditions:
 *
 *	The above copyright notice and this permission notice shall be included in 
 *	all copies or substantial portions of the Software.
 *
 *	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
 *	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
 *	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
 *	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
 *	FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 *	IN THE SOFTWARE.
 */

(function (doc, win, VJ) {
	var __ = function (q) { return doc.querySelector(q);},
		_ = function (id) { return doc.getElementById(id);},
		_create = function (tag) {return doc.createElement(tag);},
		_objGraphs = {},
		excanvas, isLoadingExCanvas = false, pendingProcess, i;

	if (!VJ) {
		VJ = {};
	}

	/**
	 *	If canvas is not supported load excanvas
	 */
	if (!(document.createElement("canvas").getContext)) {
		excanvas = document.createElement("script");
		isLoadingExCanvas = true;
		pendingProcess = [];
		excanvas.onload = function () {
			isLoadingExCanvas = false;
			console.log("!");
		};
		excanvas.src = "https://explorercanvas.googlecode.com/svn/trunk/silverlight/excanvas.js";
		document.body.appendChild(excanvas);

	}

	/**
	 *	Call this function with css.call(dom, stylename)
	 */
	function css(styleName, value)	{
		styleName.replace(/-([a-z])/g, function (g) {
			return g[1].toUpperCase();
		});
		if (value !== undefined) {
			this.style[styleName] = value;
			return this;
		} else {
			if (this.currentStyle) {
				return this.currentStyle[styleName];
			} else if (this.getComputedStyle) {
				return document.defaultView.getComputedStyle(this)[styleName];
			} else {
				return this.style[styleName];
			}
		}
	}



	function setDefaultOptions (options) {
		function defaultTrue(value) {
			return value === undefined ? true : (value || false);
		}
		options.width = parseInt(options.width || css.call(this.dom, "width") || 600);
		options.height = parseInt(options.height || css.call(this.dom, "height") || 400);
		options.autoUpdate = defaultTrue(options.autoUpdate);
		options.colors = options.colors || ["red", "blue", "green"];  // 선 색깔 바꾸는거
		options.reverseData = options.reverseData || false;
		options.marker = options.marker || "circle";
		options.max = options.max || 1;
		options.yMarkerWidth = parseInt(options.yMarkerWidth || 0);
		options.shift = defaultTrue(options.shift);
		options.dataLength = options.dataLength || this.data.length;
		return options;
	}

	/**
	 *
	 */
	VJ.graph = function (domId, data, options) {
		var graph = _objGraphs[domId];
		if (graph) {
			return graph;
		}
		graph = new _Graph(domId, data, options);
		_objGraphs[domId] = graph;
		return graph;
	}


	/**
	 *
	 *	@param {Object} options - shift, autoUpdate
	 */
	_Graph = function (domId, data, options) {
		var dom = _(domId) || __(domId),
			canvas,
			ctx,
			checkType, width, height,
			excanvas;

		if (!dom) {
			alert("Wrong dom wrapper");
			return;
		}

		if (dom.tagName.toLowerCase() === "canvas") {
			canvas = dom;
		} else {
			canvas = _create("canvas");
			if (!canvas.getContext) {
				/**
				 * 	TODO : import ExCanvas.js
				 */
				 excanvas = document.createElement("script");

			}
			dom.appendChild(canvas);
		}
		ctx = canvas.getContext("2d");

		this.dom = dom;
		this.canvas = canvas;
		this.ctx = ctx;
		this.data = data || [];
		checkType = this.data[0];
		if (checkType !== undefined && !(checkType instanceof Array)) {
			this.data = [this.data];
		}

		this.options = setDefaultOptions.call(this, options || {});

		width = this.options.width;
		height = this.options.height;

		canvas.width = width;
		canvas.height = height;
		dom.style.width = width + "px";
		dom.style.height = height + "px";

		this.render();
	};

	_Graph.prototype.appendData = function (appendingData, updateGraph) {
		var data = this.data,
			dataLength = data.length,
			options = this.options,
			i, row;
		if (options.reverseData) {
			data.push(appendingData);
			if (options.shift && dataLength > options.dataLength) {
				data.splice(0, 1);
			}
		} else {
			for (i = 0; i < dataLength; i++) {
				row = data[i];
				row.push(appendingData[i]);
				if (options.shift && row.length > options.dataLength) {
					row.splice(0, 1);
				}
			}
		}
		if (updateGraph || (updateGraph === undefined && this.options.autoUpdate)) {
			this.render();
		}
	};

	_Graph.prototype.render = function () {
		var data = this.data,
			dataLength = data.length,
			options = this.options,
			width = options.width,
			height = options.height,
			ctx = this.ctx,
			renderingData,
			renderingDataLength,
			i, j, tickWidth,
			yMarkerWidth = options.yMarkerWidth,
			max = options.max,
			heightRatio = height / max,
			leftStartPoint = 0,
			graphDataLength = options.dataLength;

		ctx.clearRect(0, 0, width, height);
		for (i = dataLength; i--;) {
			renderingData = data[i];
			renderingDataLength = renderingData.length;

			if (renderingDataLength > 0) {
				tickWidth = (width - yMarkerWidth) / graphDataLength;
				ctx.strokeStyle = options.colors[i];	//TODO : check color index
				ctx.beginPath();
				ctx.moveTo(yMarkerWidth, heightRatio * renderingData[0]);

				for (j = 1; j < renderingDataLength; j++) {
					ctx.lineTo(yMarkerWidth + tickWidth * j, heightRatio * renderingData[j]);
				}
				ctx.stroke();
			}
		}
	};


	win.VJ = VJ;
}(document, window, window.VJ));