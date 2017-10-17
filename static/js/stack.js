function getMax(arr) {
    var max = 0;
    for (var i = 0; i < arr.length; i++) {
    	// skip the all cancertype
    	if (arr[i]['cancertype'] == 'all') {
    		continue;
    	}
        var currsum = arr[i]['mut'] + arr[i]['del'] + arr[i]['amp'];
        if (max == 0 || currsum > max) {
        	max = currsum;
        }
    }
    return max;
}

var colors = ['#FBB65B', '#513551', '#de3163'];

function createPic(data) {
    var sub_width = 50;
    var max = getMax(data);

    console.log(max);
    // rescale the length for each bar

    var barScale = d3.scaleLinear()
                    .domain([0, max + 5])
                    .range([0, sub_width]);

    var total_max = data[16]['mut'] + data[16]['del'] + data[16]['amp'];
    var totalScale = d3.scaleLinear()
                        .domain([0, total_max + 5])
                        .range([0, sub_width]);

    var stack = d3.stack()
      .keys(['mut', 'amp', 'del']);

    var stackedSeries = stack(data);


    // Create a g element for each series
    var g = d3.select('g')
        .selectAll('g.series')
        .data(stackedSeries)
        .enter()
        .append('g')
        .classed('series', true)
    //  .attr('class', function(d, i) {
    //      return d3.select(this).attr('class')  + " " + d[0]['data']['day'];
    //  })
        .style('fill', function(d, i) {
            return colors[i];
        });

    // For each series create a rect element for each day
    g.selectAll('rect')
        .data(function(d) {
            console.log(d)
            return d;
        })
        .enter()
        .append('rect')
        .attr('width', function(d) {
            if (d['data']['cancertype'] == 'all') {
                return totalScale(d[1] - d[0]);
            } else {
                return barScale(d[1] - d[0]);
            }
        })
        .attr('x', function(d, i) {
            if (d['data']['cancertype'] == 'all') {
                return totalScale(d[0]) + sub_width * i;
            } else {
                return barScale(d[0]) + sub_width * i; //+ stack_width * i;
            }
        })
        .attr('class', function(d, i) {
            return d3.select(this).attr('class') + " " + d['data']['cancertype'];
        })
        .attr('height', 19);

    // add name as button on top of each rect
    var names = d3.select('svg').selectAll('text')
                    .data(data)
                    .enter()
                    .append('text')
                    .attr('x', function(d, i) {
                        return 50 * i;
                    })
                    .attr('y', 20)
                    .text(function(d) {
                        console.log(d.cancertype);
                        return d.cancertype;
                    })

}