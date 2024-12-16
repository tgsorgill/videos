from manim import *

class WillansFormula(Scene):
    def construct(self):

        # Title for the scene
        title = Tex("Willans' Formula for the N-th Prime Number")
        title.set_color(BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Willans' formula representation (large display at the start)
        formula = MathTex(
            r"p_N = 1 + \sum_{k=1}^{2^N}\Big\lfloor \frac{N}{\sum_{j=1}^k\lfloor\cos^2\big(\pi\big(\frac{j! + 1}{j}\big)\big)\rfloor}\Big\rfloor"
        )
        formula.scale(1.5)  # Make formula large at the start
        formula.next_to(title, DOWN)

        # Display the formula
        self.play(Write(formula), run_time=3)
        self.wait(2)

        # Shrink the formula for further explanations
        self.play(formula.animate.scale(0.8))

        # Breakdown explanation of the formula
        explanation = VGroup(
            Tex(r"$p_N$: The N-th prime number", color=YELLOW),
            Tex(r"$\lfloor x \rfloor$: The floor function, rounding down to the nearest integer", color=WHITE),
            Tex(r"$j!$: The factorial of $j$, e.g., $3! = 3 \times 2 \times 1 = 6$", color=WHITE),
            Tex(r"$\cos^2$: The square of the cosine function", color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        explanation.next_to(formula, 2 * DOWN)

        # Fade in each explanation line
        for line in explanation:
            self.play(FadeIn(line))
            self.wait(1)

        self.wait(2)

        # Highlight key parts of the formula
        self.play(
            Indicate(formula[0][4:6]),  # Highlight "N"
            Indicate(formula[0][9:10]),  # Highlight "k"
            Indicate(formula[0][33:39]),  # Highlight cosine term
            run_time=2
        )

        # Fade out the formula and explanation before the example
        self.play(FadeOut(formula), FadeOut(explanation), FadeOut(title))

        # Add an example
        example_title = Tex("Example: Compute $p_3$, the 3rd prime number")
        example_title.set_color(GREEN)
        example_title.to_edge(UP)
        self.play(Write(example_title))
        self.wait(1)

        example_calculation = MathTex(
            r"p_3 = 1 + \sum_{k=1}^{2^3}\Big\lfloor \frac{3}{\sum_{j=1}^k\lfloor\cos^2\big(\pi\big(\frac{j! + 1}{j}\big)\big)\rfloor}\Big\rfloor"
        )
        example_calculation.scale(0.8)
        example_calculation.next_to(example_title, DOWN)

        self.play(Write(example_calculation), run_time=3)
        self.wait(2)

        # Show result for p_3
        result = MathTex(r"p_3 = 5", color=YELLOW)
        result.next_to(example_calculation, 2 * DOWN)

        self.play(Transform(example_calculation, result), run_time=2)
        self.wait(2)

        # End scene with the example emphasized
        self.play(Indicate(result, scale_factor=1.2))
        self.wait(2)

        # Clear the scene
        self.clear()
