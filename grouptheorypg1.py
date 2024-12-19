from manim import *
class GroupTheoryPageOne(Scene):
	def construct(self):
		# Consider a simple example --- 2 x 2 real matrices with non-zero determinant
		matrixA = Matrix([
			["a", "b"],
			["c", "d"]	
		]).shift(LEFT*1.5)
		label = MathTex("A=").next_to(matrixA, LEFT)
		detA = MathTex("\\det(A)=ad-bc\\neq 0").shift(RIGHT*2.5)
		#self.add(matrixA, label, detA)
		self.play(Write(label), Write(matrixA))
		self.play(Write(detA))
		self.wait(1)
		self.play(FadeOut(*self.mobjects))