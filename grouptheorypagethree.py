from manim import *
class GroupTheoryPageThree(Scene):
	def construct(self):
		# List some properties of GL(2,R) = {2 x 2 real matrices with non-zero determinant}
		self.wait(5)

		# Associative Property
		property1 = MathTex("\\text{Associative Property}").set_color(RED).shift(UP*3.5)
		statement1 = MathTex("(AB)C = A(BC)").set_color(RED).shift(UP*2.5)
		proofAssocProp = MathTex(
			r"\text{Proof. }[(AB)C]_{ij} &= \sum_{l=1}^{2}\sum_{k=1}^{2}a_{ik}b_{kl}c_{lj}\\",
			r"&= \sum_{k=1}^{2}\sum_{l=1}^{2}a_{ik}b_{kl}c_{lj} \\",
			r"&= \sum_{k=1}^{2}a_{ik}\sum_{l=1}^{2}b_{kl}c_{lj} \\",
			r"&= [A(BC)]_{ij} "
		).shift(DOWN*1)
		self.play(Write(property1), Write(statement1))
		self.wait(4)
		self.play(Write(proofAssocProp[0]))
		self.play(Write(proofAssocProp[1]))
		self.play(Write(proofAssocProp[2]))
		self.play(Write(proofAssocProp[3]))
		self.play(FadeOut(*self.mobjects)) # clear screen

		# Identity
		property2 = MathTex("\\text{Identity}").set_color(RED).shift(UP*2)
		matrixI = Matrix([["1", "0"], ["0", "1"]]).shift(LEFT*2)
		labelI = MathTex("I=").next_to(matrixI, LEFT)
		statement2 = MathTex("AI=IA=A").shift(RIGHT*2)
		self.play(Write(property2), Write(labelI), Write(matrixI), Write(statement2))
		self.wait(4)
		self.play(FadeOut(*self.mobjects))
		
		# Inverse
		property3 = MathTex("\\text{Inverse}").set_color(RED).shift(UP*2)
		inverse = MathTex("AA^{-1}=A^{-1}A=I").shift(RIGHT*2)
		detReq = MathTex("\\det(A)\\neq 0").shift(LEFT*2)
		self.play(Write(property3), Write(detReq), Write(inverse))
		self.wait(8)
		self.play(FadeOut(*self.mobjects))


		