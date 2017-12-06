// data

var bardata = [20, 30, 105, 15, 85];

var height = 400,
    width = 1200,
    barWidth = 15,
    barOffset = 5;

var row_max = 350;
var row_data = [[[30, 300, 500], [40, 60, 200]],
				[[20, 400, 600], [100, 150, 800]]];

var sgadata = {"CDKN2A": {"0": [0, 0, 0], "1": [11, 11, 80], "2": [0, 5, 37], "3": [1, 3, 4], "4": [13, 13, 76], "5": [2, 2, 125], "6": [101, 101, 244], "7": [4, 4, 17], "8": [2, 2, 12], "9": [1, 1, 8], "10": [13, 14, 80], "11": [20, 21, 57], "12": [0, 5, 17], "13": [1, 1, 6], "14": [1, 1, 2], "15": [6, 6, 29], "16": [1, 1, 1]}, "TP53": {"0": [0, 0, 0], "1": [95, 95, 100], "2": [245, 245, 251], "3": [104, 104, 106], "4": [129, 129, 131], "5": [66, 66, 71], "6": [316, 317, 320], "7": [17, 17, 17], "8": [4, 4, 4], "9": [41, 41, 43], "10": [186, 186, 189], "11": [108, 108, 111], "12": [269, 273, 275], "13": [44, 44, 77], "14": [57, 57, 57], "15": [80, 80, 83], "16": [41, 41, 41]}, "PTEN": {"0": [0, 0, 0], "1": [7, 9, 17], "2": [33, 34, 76], "3": [12, 12, 19], "4": [6, 6, 11], "5": [65, 65, 88], "6": [11, 11, 28], "7": [15, 16, 20], "8": [5, 5, 5], "9": [2, 2, 7], "10": [4, 4, 9], "11": [13, 13, 27], "12": [1, 2, 13], "13": [14, 15, 90], "14": [4, 4, 5], "15": [8, 9, 14], "16": [132, 134, 143]}, "PIK3CA": {"0": [0, 0, 0], "1": [39, 45, 45], "2": [285, 317, 318], "3": [47, 47, 47], "4": [11, 38, 38], "5": [19, 23, 23], "6": [83, 165, 165], "7": [12, 20, 20], "8": [2, 2, 2], "9": [3, 5, 5], "10": [22, 23, 25], "11": [14, 79, 79], "12": [3, 65, 65], "13": [13, 25, 30], "14": [8, 8, 8], "15": [29, 35, 35], "16": [99, 105, 106]}, "ARID1A": {"0": [0, 0, 0], "1": [52, 53, 56], "2": [20, 21, 25], "3": [13, 13, 15], "4": [11, 11, 13], "5": [2, 2, 2], "6": [19, 19, 22], "7": [23, 23, 24], "8": [9, 9, 9], "9": [11, 12, 14], "10": [30, 31, 32], "11": [9, 9, 9], "12": [1, 2, 5], "13": [6, 6, 9], "14": [1, 1, 1], "15": [39, 39, 43], "16": [63, 64, 65]}, "RYR2": {"0": [0, 0, 0], "1": [33, 36, 36], "2": [41, 110, 111], "3": [30, 30, 30], "4": [25, 26, 26], "5": [26, 26, 26], "6": [63, 66, 66], "7": [16, 17, 17], "8": [6, 6, 7], "9": [20, 29, 29], "10": [141, 145, 145], "11": [54, 55, 55], "12": [10, 24, 25], "13": [18, 20, 33], "14": [12, 12, 12], "15": [21, 23, 24], "16": [23, 27, 27]}, "EGFR": {"0": [0, 0, 0], "1": [3, 14, 14], "2": [4, 19, 20], "3": [4, 6, 7], "4": [3, 20, 21], "5": [62, 170, 170], "6": [20, 66, 67], "7": [8, 8, 8], "8": [0, 0, 1], "9": [5, 8, 8], "10": [55, 77, 79], "11": [3, 11, 11], "12": [8, 9, 10], "13": [4, 4, 5], "14": [1, 2, 2], "15": [5, 13, 14], "16": [3, 5, 5]}, "FAT1": {"0": [0, 0, 0], "1": [24, 25, 31], "2": [15, 19, 31], "3": [8, 8, 12], "4": [3, 4, 10], "5": [4, 4, 6], "6": [106, 109, 143], "7": [17, 17, 19], "8": [13, 13, 14], "9": [2, 2, 8], "10": [33, 33, 43], "11": [18, 18, 25], "12": [6, 7, 16], "13": [4, 4, 4], "14": [5, 5, 6], "15": [10, 11, 14], "16": [22, 22, 23]}, "BAGE2": {"0": [0, 0, 0], "1": [30, 33, 35], "2": [2, 10, 25], "3": [2, 2, 3], "4": [34, 34, 37], "5": [1, 2, 3], "6": [71, 77, 81], "7": [8, 8, 9], "8": [2, 2, 2], "9": [3, 3, 3], "10": [101, 105, 111], "11": [3, 8, 13], "12": [0, 4, 11], "13": [44, 46, 49], "14": [1, 1, 2], "15": [30, 30, 36], "16": [0, 0, 0]}, "MUC4": {"0": [0, 0, 0], "1": [8, 14, 14], "2": [40, 61, 62], "3": [33, 33, 33], "4": [45, 76, 76], "5": [7, 8, 8], "6": [32, 106, 106], "7": [62, 67, 67], "8": [16, 16, 16], "9": [10, 12, 12], "10": [21, 23, 26], "11": [11, 62, 62], "12": [4, 56, 57], "13": [6, 12, 24], "14": [4, 4, 4], "15": [12, 17, 19], "16": [13, 20, 20]}, "PCDHAC2": {"0": [0, 0, 0], "1": [5, 5, 5], "2": [5, 7, 8], "3": [6, 6, 6], "4": [4, 4, 4], "5": [0, 0, 0], "6": [8, 8, 8], "7": [3, 69, 69], "8": [0, 0, 0], "9": [4, 4, 4], "10": [2, 2, 3], "11": [1, 1, 2], "12": [1, 4, 5], "13": [2, 4, 7], "14": [1, 1, 1], "15": [5, 5, 5], "16": [2, 2, 2]}, "CSMD3": {"0": [0, 0, 0], "1": [30, 44, 44], "2": [13, 138, 139], "3": [23, 28, 29], "4": [24, 41, 41], "5": [7, 10, 11], "6": [92, 124, 124], "7": [15, 18, 18], "8": [5, 5, 5], "9": [19, 41, 43], "10": [142, 156, 156], "11": [63, 66, 68], "12": [19, 90, 92], "13": [16, 38, 49], "14": [4, 10, 10], "15": [39, 46, 48], "16": [25, 28, 28]}, "LRP1B": {"0": [0, 0, 0], "1": [26, 28, 45], "2": [21, 25, 35], "3": [21, 21, 24], "4": [34, 35, 65], "5": [6, 7, 10], "6": [87, 90, 147], "7": [14, 14, 16], "8": [6, 6, 9], "9": [9, 9, 12], "10": [125, 126, 140], "11": [50, 53, 70], "12": [12, 17, 33], "13": [21, 22, 55], "14": [10, 10, 10], "15": [40, 40, 47], "16": [9, 9, 15]}, "CSMD1": {"0": [0, 0, 0], "1": [17, 17, 37], "2": [23, 35, 109], "3": [15, 15, 29], "4": [23, 30, 53], "5": [4, 6, 12], "6": [39, 39, 140], "7": [19, 21, 37], "8": [5, 5, 7], "9": [13, 14, 29], "10": [81, 84, 107], "11": [24, 24, 49], "12": [0, 1, 38], "13": [12, 12, 57], "14": [9, 9, 20], "15": [34, 37, 45], "16": [14, 16, 21]}, "TTN": {"0": [0, 0, 0], "1": [111, 113, 114], "2": [148, 152, 153], "3": [88, 88, 88], "4": [66, 67, 67], "5": [63, 63, 63], "6": [210, 219, 219], "7": [89, 93, 93], "8": [28, 31, 31], "9": [43, 44, 44], "10": [184, 184, 184], "11": [100, 102, 102], "12": [44, 50, 50], "13": [52, 53, 64], "14": [31, 31, 31], "15": [94, 95, 96], "16": [60, 60, 61]}, "ZFHX4": {"0": [0, 0, 0], "1": [21, 27, 27], "2": [24, 99, 100], "3": [28, 32, 32], "4": [11, 20, 20], "5": [2, 3, 3], "6": [51, 65, 65], "7": [11, 14, 14], "8": [3, 3, 3], "9": [7, 18, 18], "10": [106, 120, 122], "11": [53, 55, 55], "12": [11, 30, 30], "13": [4, 24, 28], "14": [7, 10, 10], "15": [22, 29, 29], "16": [20, 21, 21]}, "MUC16": {"0": [0, 0, 0], "1": [70, 72, 73], "2": [79, 88, 88], "3": [46, 46, 47], "4": [43, 43, 45], "5": [38, 39, 39], "6": [101, 105, 107], "7": [65, 65, 66], "8": [16, 16, 16], "9": [33, 33, 34], "10": [157, 158, 162], "11": [68, 69, 70], "12": [17, 29, 32], "13": [39, 39, 39], "14": [10, 10, 10], "15": [54, 54, 56], "16": [35, 41, 42]}, "KRAS": {"0": [0, 0, 0], "1": [5, 8, 9], "2": [5, 17, 20], "3": [80, 81, 81], "4": [2, 12, 13], "5": [1, 2, 3], "6": [1, 5, 5], "7": [1, 1, 1], "8": [2, 2, 2], "9": [3, 4, 4], "10": [126, 149, 151], "11": [1, 3, 3], "12": [6, 43, 43], "13": [0, 2, 4], "14": [27, 31, 31], "15": [14, 29, 29], "16": [38, 43, 43]}, "FRG1B": {"0": [0, 0, 0], "1": [41, 49, 49], "2": [25, 37, 38], "3": [0, 15, 15], "4": [15, 21, 21], "5": [9, 10, 10], "6": [96, 108, 108], "7": [14, 14, 14], "8": [31, 31, 31], "9": [0, 1, 1], "10": [81, 87, 88], "11": [0, 7, 8], "12": [0, 8, 8], "13": [74, 75, 75], "14": [0, 7, 7], "15": [25, 31, 31], "16": [0, 2, 2]}, "PCDHGC5": {"0": [0, 0, 0], "1": [3, 3, 3], "2": [3, 5, 6], "3": [2, 2, 2], "4": [4, 4, 4], "5": [0, 0, 0], "6": [6, 6, 6], "7": [6, 71, 71], "8": [1, 1, 1], "9": [0, 0, 0], "10": [3, 3, 4], "11": [1, 1, 2], "12": [2, 7, 8], "13": [1, 3, 5], "14": [1, 1, 1], "15": [4, 4, 4], "16": [2, 2, 2]}};


//var obj = JSON.parse(sgadata);
d3.json("home/", function(data){
	d = data;
    function initChart(inputdata){
        //all your code f initChart here
        var rowmap = d3.scale.linear()
				.domain([0, row_max])
				.range([0, 70])

		var row_colors = ['#00cc66', '#ff4f49', '#00768f'];

		var color_chosen = {'SM': '#00cc66', 'CN_AMP':'#ff4f49', 'CN_DEL': '#00768f'};

		var maxvalues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
		var cancer_types = [' ','BRCA', 'BLCA', 'COAD', 'ESCA','GBM','HNSC','KIRC','KIRP','LIHC','LUAD','LUSC','OV','PRAD','READ','STAD','UCEC']
		var rows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
		var colors = d3.scale.linear()
						.domain([0, d3.max(bardata)])
						.range(['#819090', '#000000']);
        var chart = d3.select('#chart').append('svg')
			    .attr('width', width)
			    .attr('height', 1000)
			    .style('position', 'absolute');
	    var firstline = chart.selectAll('text').data(cancer_types)
					.enter().append('text')
						.attr('width', 70)
						.attr('height', 17)
						.attr('y', 14)
						.attr('x', function(d, i) {
							return i * 70;
						})
						.text(function(d) {
							return d;
						})
						.attr('fill', 'black');
		var legend = d3.select('#legend').append('svg')
						.attr('width', 100)
						.attr('height', 100)
						.style('position', 'absolute');
		var updated = {}
		arr = []
		var list = inputdata['list']
		inputdata = inputdata['data']
		console.log(inputdata)
		for (item in inputdata) {
			updated[item] = {}
			for (var i in cancer_types) {
				var t = cancer_types[i];
				if (t != ' ') {
					updated[item][t] = [];
					if (typeof inputdata[item]['SM'][t] === 'undefined') {
						updated[item][t].push(0);
					} else {
						updated[item][t].push(inputdata[item]['SM'][t]);
					}
					if (typeof inputdata[item]['CN_AMP'][t] === 'undefined') {
						updated[item][t].push(updated[item][t][0]);
					} else {
						updated[item][t].push(inputdata[item]['CN_AMP'][t] + updated[item][t][0]);
					}
					if (typeof inputdata[item]['CN_DEL'][t] === 'undefined') {
						updated[item][t].push(updated[item][t][1]);
					} else {
						updated[item][t].push(inputdata[item]['CN_DEL'][t] + updated[item][t][1]);
					}

				}

			}
		}
		sgadata = updated;
		//add blocks for each line with different cancer types

		legends = ['Somatic mutations', 'Copy number alteration - amplification', 'Copy number alteration - deletion'];
		legend.selectAll('.rect').data(row_colors)
				.enter().append('rect')
				.attr('y', function(d, i) {
					return i * 15
				})
				.attr('width', 15)
				.attr('height', 15)
				.style('fill', function(d, i) {
					return row_colors[i];
				})
				.append('text')
				.text(function(d, i) {
					return legends[i];
				})
				.style('color', 'black');

		//create the rows
		chart.selectAll('.rect').data(rows)
								.enter().append('rect')
								.attr('transform', 'translate(0, -13)')
								.attr('width', 1200)
								.attr('height', 15)
								.attr('x', 0)
								.attr('y', function(d, i) {
									console.log('get here!!!!!')
									return 30 * (i + 1);
								})
								.style('fill', function(d, i) {
									if (i % 2 == 0) {
										return "#3E9583";
									} else {
										return "#ffffff";
									}
								})
								.style('opacity', 0.1);



		for (row = 0; row < 20; row++) {
			for (col = 0; col < 16; col++) {
				chart.append('rect')
				.attr('transform', 'translate(80, 18)')
				.attr('x', 70 * col)
				.attr('y', 30 * row)
				.attr('width', 50)
				.attr('height', 15)
				.style('fill', 'grey')
				.style('opacity', 0.5)
			}
		}


		//chart.append("p").data(cancer_types)
		//		.text("function(d) return d;");



		var tooltip = d3.select('#tooltip').append('div')
						.style('position', 'relative')
						.style('padding', '0 10px')
						.style('background', 'white')
						.style('opacity', 0)
						.style('y', 1100);


		var row = 0;

		new_scale = d3.scale.linear()
						.domain([0, 1])
						.range([0, 70]);

		var tempColor;
		var tempHeight;
		var tempWidth;
		// for (var key in inputdata) {
		// 	console.log('check data');
		// 	console.log(inputdata[key]);
		// }

		for (var idx in list) {
		  var key = list[idx]
		  if (sgadata.hasOwnProperty(key)) {
		  	   var column = 0;
		      //console.log(row_max);
		      chart.append("a")
		      		.classed(cancer_types[column], true)
		      		.attr("xlink:href", "http://www.google.com")
		      		.append("text")
					.attr("class", "label")
					.attr("y", 30 * (row + 1))
					.attr("dy", ".35em")
					.attr('font-size', 15)
					.text(key)
					.on('mouseover', function(d) {
						tempColor = this.style.fill;
						d3.select(this)
					        .style('background-color', "#819090")
					        .style('fill', '#819090')
					})
					.on('mouseout', function(d) {
						d3.select(this)
					        .style('opacity', 1)
					        .style('fill', tempColor)
					});

		      for (var sga in sgadata[key]) {
		      		if (sgadata[key].hasOwnProperty(sga)) {
		      			//console.log(sga + "-->" + sgadata[key][sga] + " col " + column);
		      			var data = sgadata[key][sga]
		      			chart.selectAll('.rect').data(data)
								.enter().append('rect')
									.style('fill', function(d, i) {
										//console.log(i);
										return row_colors[i];
									})
									.attr('width', function(d, i) {
										//console.log(rowmap(d));
										if (i == 0) {
											return new_scale(d);
										} else{
											return new_scale(d) - new_scale(data[i - 1]);
										}
									})
									.attr('height', barWidth)
									.attr('x', function(d, i) {								
										if (i == 0) {
											return 70 * column;
										} else {
											//console.log("current data " + (data[i - 1] + rowmap(data[i - 1])));
											return 70 * column + new_scale(data[i - 1]);
										}
									})
									.attr('y', function() {
										return (row + 1) * 30;
									})
									.attr('transform', 'translate(80, -13)')
									.on('mouseover', function(d) {
										tempColor = this.style.fill;
										tempWidth = this.style.width;
										tempHeight = this.style.height;

										tooltip.transition()
												.style('opacity', 0.9)
										tooltip.html('value ' + d)
										d3.select(this)
							                .style('opacity', 0.8)
							                //.style('width', 100)
							                //.style('height', 15)
									})
									.on('mouseout', function(d) {
										d3.select(this)
							                .style('opacity', 1)
							                .style('fill', tempColor)
							                //.style('width', tempWidth)
							                //.style('height', tempHeight)
									})
									.classed(cancer_types[column], true);

		      		}
		      		column = column + 1;
		      }
		  }
		  row = row + 1;
		}
        
    };
    initChart(data);
})














// legend
//d3.select('.legend').html('<div class="block"></div><div>0 - 10</div>')






