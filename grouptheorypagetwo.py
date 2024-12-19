from manim import *
class GroupTheoryPageTwo(Scene):
	def construct(self):
		# Review Matrix Multiplication
		reviewMult = MathTex("\\text{Matrix Multiplication}").set_color(RED)
		reviewMult.shift(UP*3)
		matrixA = Matrix([["a_{11}", "a_{12}"], ["a_{21}", "a_{22}"]])
		matrixB = Matrix([["b_{11}", "b_{12}"], ["b_{21}", "b_{22}"]])
		matrixA.shift(LEFT*1, UP*1)
		matrixB.shift(RIGHT*1.8, UP*1)
		matrixAB = Matrix([["a_{11}b_{11}+a_{12}b_{21}", "a_{11}b_{12}+a_{12}b_{22}"], 
					["a_{21}b_{11}+a_{22}b_{21}", "a_{21}b_{12}+a_{22}b_{22}"]],
				h_buff=3.5, # Horizontal buffer between columns
		)
		matrixAB.shift(DOWN*1)
		
		# Create boxes for highlighting rows and columns
		row_box_1 = SurroundingRectangle(matrixA.get_rows()[0], color=RED)
		row_box_2 = SurroundingRectangle(matrixA.get_rows()[1], color=RED)
		col_box_1 = SurroundingRectangle(matrixB.get_columns()[0], color=BLUE)
		col_box_2 = SurroundingRectangle(matrixB.get_columns()[1], color=BLUE)

		label = MathTex("AB=").next_to(matrixA, LEFT)
		label2 = MathTex("=").next_to(matrixAB, LEFT)

		# Write Title and AB=[matrixA][matrixB]
		self.play(Write(reviewMult), Write(label), Write(matrixA), Write(matrixB))
		self.wait(2)
		
		# Show the brackets first
		self.play(Write(label2), Write(matrixAB.get_brackets())) 

		# Get matrix entries of AB
		entriesAB = matrixAB.get_entries()

		#Highlight row of A and column of B before displaying entry of AB
		self.play(Create(row_box_1), Create(col_box_1))
		self.play(FadeIn(entriesAB[0]))
		self.wait(1)
		self.remove(row_box_1, col_box_1)

		self.play(Create(row_box_1), Create(col_box_2))
		self.play(FadeIn(entriesAB[1]))
		self.wait(1)
		self.remove(row_box_1, col_box_2)

		self.play(Create(row_box_2), Create(col_box_1))
		self.play(FadeIn(entriesAB[2]))
		self.wait(1)
		self.remove(row_box_2, col_box_1)

		self.play(Create(row_box_2), Create(col_box_2))
		self.play(FadeIn(entriesAB[3]))
		self.wait(1)
		#self.remove(row_box_2, col_box_2)

		self.wait(1)
		self.play(FadeOut(*self.mobjects)) # Fade Out this scene

