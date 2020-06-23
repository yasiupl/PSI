if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register('/service-worker.js');
    });
}

const app = new Vue({
    el: '#app',
    data: {
        u: 1,
        p: 1,
        i: 1,
        d: 1,
        websocket: io(),
        series: null,
    },
    methods: {
        send() {
            this.websocket.emit("update", [this.u, this.p, this.i, this.d]);
        }
    },
    mounted() {
        const chart = new SmoothieChart({minValue:-5,maxValue:5}),
            canvas = document.getElementById('smoothie-chart');
        this.series = new TimeSeries();

        chart.addTimeSeries(this.series, { lineWidth: 2, strokeStyle: '#ff5722' });
        chart.streamTo(canvas, 500);

        this.websocket.on("response", (liczba) => {
            const now = new Date().getTime();
            this.series.append(now, liczba);

            liczba = (liczba * 10000).toFixed() / 10000;
            console.log(liczba);
        });
    }
})