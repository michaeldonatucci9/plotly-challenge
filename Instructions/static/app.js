d3.json("samples.json").then(
    data => {
        let trace1 = {
            x: data.map(d=> d.otu_ids),
            y: data.map(d=> d.sample_values),
            title: "Species Count"
        }
        let trace2 = {
            x: data.map(d=> d.sample_values),
            y: data.map(d=> d.otu_ids),
            title: "Diversity"
        }
        // let trace3 = {
        //     x: data.map(d=> d.metadata),
        //     y: data.map(d=> d.otu_labels)
        // }

        let plotData = [trace1, trace2]

        let plotLayout = {
            title: "Belly Button Diversity Michael"
        }
        
        Plotly.newPlot('myPlot', plotData, plotLayout)
    }
)
