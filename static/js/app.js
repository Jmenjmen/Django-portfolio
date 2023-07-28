gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

ScrollSmoother.create({
	wrapper: '.wrapper',
	content: '.content',
	smooth: 1.5,
	effects: true,
})

gsap.fromTo('.about-project', { opacity: 1 }, {
	 opacity: 0.7,
	 scrollTrigger: {
		trigger: '.about-project',
		start: 'start',
		end: '700',
		scrub: true,
	}
	 })
