(function(){
    // Lightweight GSAP-driven compare interaction.
    if(typeof gsap === 'undefined') return;

    const card = document.getElementById('compare-card');
    if(!card) return;

    const leftPanel = card.querySelector('.panel.left');
    const rightPanel = card.querySelector('.panel.right');
    const toggle = document.getElementById('compare-toggle');

    // Entrance animation
    gsap.from(card, {opacity:0, y:30, duration:0.8, ease:'power3.out'});
    gsap.from([leftPanel, rightPanel], {opacity:0, y:20, duration:0.9, stagger:0.08, ease:'power3.out'});

    // Create a subtle hover microinteraction
    [leftPanel, rightPanel].forEach(p=>{
        p.addEventListener('mouseenter', ()=> gsap.to(p, {scale:1.02, boxShadow:'0 20px 40px rgba(2,6,23,0.6)', duration:0.35}));
        p.addEventListener('mouseleave', ()=> gsap.to(p, {scale:1, boxShadow:'none', duration:0.35}));
    });

    // Toggle-driven compare: slide slight offsets and highlight
    const tl = gsap.timeline({paused:true});
    tl.to(leftPanel, {xPercent:-6, duration:0.6, ease:'power3.out'}, 0)
      .to(rightPanel, {xPercent:6, duration:0.6, ease:'power3.out'}, 0)
      .to(leftPanel, {filter:'grayscale(0)', opacity:1, duration:0.6}, 0)
      .to(rightPanel, {filter:'grayscale(0)', opacity:1, duration:0.6}, 0)
      .to(card, {boxShadow:'0 30px 80px rgba(2,6,23,0.7)', duration:0.6}, 0);

    if(toggle){
        toggle.addEventListener('click', ()=>{
            if(tl.reversed() || tl.paused()) { tl.play(); toggle.setAttribute('aria-pressed','true'); toggle.innerText='Reset'; }
            else { tl.reverse(); toggle.setAttribute('aria-pressed','false'); toggle.innerText='Compare'; }
        });
    }

    // Animate metric numbers if numeric (fallback: simple pulse on toggle)
    function animateMetric(side){
        const nodes = card.querySelectorAll('.metric-val[data-side="'+side+'"]');
        nodes.forEach(n=>{
            const text = n.innerText || '';
            const numeric = parseFloat(text.replace(/[^0-9\.]/g,''));
            if(!isNaN(numeric)){
                gsap.fromTo(n, {innerText:0}, {innerText:numeric, duration:0.9, roundProps:'innerText', onUpdate:function(){ n.innerText = Math.round(this.targets()[0].innerText) + (text.replace(/[0-9\.]/g,'')); }});
            } else {
                // small pulse
                gsap.fromTo(n, {scale:0.98}, {scale:1, duration:0.6, yoyo:true, repeat:1});
            }
        });
    }

    if(toggle){
        toggle.addEventListener('click', ()=>{
            setTimeout(()=>{ animateMetric('left'); animateMetric('right'); }, 220);
        });
    } else {
        // no toggle present — animate metrics once on load for visual polish
        setTimeout(()=>{ animateMetric('left'); animateMetric('right'); }, 420);
    }

    // Respect reduced motion
    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
        tl.duration(0);
    }
})();
