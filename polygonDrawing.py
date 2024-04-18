from manim import *
import numpy as np
import math

class aplusbSq(Scene):
    def construct(self):

        aPlusb=5       
        bigS=Square(aPlusb).to_edge(DOWN)

        self.add(bigS)

        a=bigS.side_length*2/aPlusb
        b=bigS.side_length-a

        ul=bigS.get_corner(UL)
        dl=bigS.get_corner(DL)
        ur=bigS.get_corner(UR)
        abTop=ul+RIGHT*a
        abLeft=ul+DOWN*a
        abRight=ur+DOWN*a
        abBottom=dl+RIGHT*a

        aBrTop=Brace(Line(ul,abTop),UP)
        aBrTopLabel=aBrTop.get_tex("a")
        bBrTop=Brace(Line(abTop,ur),UP)
        bBrTopLabel=bBrTop.get_tex("b")
        aBrLeft=Brace(Line(ul,abLeft),LEFT)
        aBrLeftLabel=aBrLeft.get_tex("a")
        bBrLeft=Brace(Line(abLeft,dl),LEFT)
        bBrLeftLabel=bBrLeft.get_tex("b")
        self.play(FadeIn(aBrTop,aBrTopLabel,bBrTop,bBrTopLabel))
        self.play(FadeIn(aBrLeft,aBrLeftLabel,bBrLeft,bBrLeftLabel))

        L1=Line(abTop,abBottom)
        L2=Line(abLeft,abRight)
        self.play(Write(L1))
        self.play(Write(L2))
        aSq=Square(a,color=YELLOW).set_opacity(0.7).align_to(bigS,UL).set_stroke(None)

        a1=aBrTopLabel.copy()
        a1.generate_target()
        a1.target.move_to(aSq.get_center())
        a2=aBrLeftLabel.copy()
        a2.generate_target()
        a2.target.move_to(aSq.get_center())

        self.play(MoveToTarget(a1),MoveToTarget(a2))
        aSqTex=MathTex("a^2").move_to(aSq.get_center())
        self.play(FadeOut(a1,a2),FadeIn(aSqTex))
        self.play(FadeIn(aSq))

        bSq=Square(b,color=PURE_RED).set_opacity(0.7).align_to(bigS,DR).set_stroke(None)
        b1=bBrTopLabel.copy()
        b1.generate_target()
        b1.target.move_to(bSq.get_center())
        b2=bBrLeftLabel.copy()
        b2.generate_target()
        b2.target.move_to(bSq.get_center())

        self.play(MoveToTarget(b1),MoveToTarget(b2))
        bSqTex=MathTex("b^2").move_to(bSq.get_center())
        self.play(FadeOut(b1,b2),FadeIn(bSqTex))
        self.play(FadeIn(bSq))

        abRect=Rectangle(width=b,height=a,color=PURE_GREEN).set_opacity(0.7).align_to(bigS,UR).set_stroke(None)
        b1=bBrTopLabel.copy()
        b1.generate_target()
        b1.target.move_to(abRect.get_center())
        a2=aBrLeftLabel.copy()
        a2.generate_target()
        a2.target.move_to(abRect.get_center())

        self.play(MoveToTarget(b1),MoveToTarget(a2))
        abTex=MathTex("ab").move_to(abRect.get_center())
        self.play(FadeOut(b1,a2),FadeIn(abTex))
        self.play(FadeIn(abRect))

        baRect=Rectangle(width=a,height=b,color=PURE_GREEN).set_opacity(0.7).align_to(bigS,DL).set_stroke(None)
        b2=bBrLeftLabel.copy()
        b2.generate_target()
        b2.target.move_to(baRect.get_center())
        a1=aBrTopLabel.copy()
        a1.generate_target()
        a1.target.move_to(baRect.get_center())

        self.play(MoveToTarget(b2),MoveToTarget(a1))
        baTex=MathTex("ab").move_to(baRect.get_center())
        self.play(FadeOut(b2,a1),FadeIn(baTex))
        self.play(FadeIn(baRect))

        aPlusbSqTex=MathTex("({{a}}+{{b}})\\times({{a}}+{{b}})={{a^2}}+{{ab}}+{{ab}}+{{b^2}}").to_edge(UP)

        self.play(
            ReplacementTransform(aBrTopLabel.copy(),aPlusbSqTex[1]),
            ReplacementTransform(bBrTopLabel.copy(),aPlusbSqTex[3])
        )
        self.play(Write(aPlusbSqTex[0]),Write(aPlusbSqTex[2]),Write(aPlusbSqTex[4][0]))
        self.play(
            ReplacementTransform(aBrLeftLabel.copy(),aPlusbSqTex[5]),
            ReplacementTransform(bBrLeftLabel.copy(),aPlusbSqTex[7])
        )
        self.play(Write(aPlusbSqTex[4][2]),Write(aPlusbSqTex[6][0]),Write(aPlusbSqTex[8][0]))
        self.play(Write(aPlusbSqTex[4][1]),Write(aPlusbSqTex[8][1]))
        self.play(ReplacementTransform(aSqTex.copy().set_color(YELLOW),aPlusbSqTex[9].set_color(YELLOW)))
        self.play(ReplacementTransform(abTex.copy().set_color(PURE_GREEN),aPlusbSqTex[11].set_color(PURE_GREEN)))
        self.play(ReplacementTransform(baTex.copy().set_color(PURE_GREEN),aPlusbSqTex[13].set_color(PURE_GREEN)))
        self.play(ReplacementTransform(bSqTex.copy().set_color(PURE_RED),aPlusbSqTex[15].set_color(PURE_RED)))
        self.play(Write(aPlusbSqTex[10]),Write(aPlusbSqTex[12]),Write(aPlusbSqTex[14]))
#        self.add(aPlusbSqTex)
        self.wait(2)
        equalTex=MathTex("=").move_to(aPlusbSqTex[8][1].get_center())
        eq1=MathTex("(a+b)^2").next_to(equalTex,LEFT)
        eq2=MathTex("a^2").next_to(equalTex).set_color(YELLOW)
        eq3=MathTex("+").next_to(eq2)
        eq4=MathTex("2ab").next_to(eq3).set_color(PURE_GREEN)
        eq5=MathTex("+").next_to(eq4)
        eq6=MathTex("b^2").next_to(eq5).set_color(PURE_RED)

        finalTex=VGroup(eq1,eq2,eq3,eq4,eq5,eq6,equalTex)

        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(ReplacementTransform(aPlusbSqTex,finalTex))
        self.wait(6)

class aplusbCube(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()

        light = self.camera.light_source
        light.move_to([-25, -20, 20])

        cubeAll=Cube(5,fill_opacity=0.0,fill_color=PURE_GREEN).to_edge(DOWN)
        
        def Cuboid(xLen:float, yLen:float, zLen:float, myColor) -> VGroup:
            vertex_coords=[
                [0   ,   0,   0],
                [0   ,yLen,   0],
                [xLen,yLen,   0],
                [xLen,   0,   0],
                [0   ,   0,zLen],
                [0   ,yLen,zLen],
                [xLen,yLen,zLen],
                [xLen,   0,zLen]
            ]
            faces_list=[
                [0,1,2,3],
                [4,5,6,7],
                [0,1,5,4],
                [1,2,6,5],
                [2,3,7,6],
                [3,0,4,7]
            ]
            cuboid=VGroup()
            for faces in faces_list:
                cuboid.add(Polygon(*itemgetter(*faces)(vertex_coords)).set_fill(color=myColor,opacity=0.7).set_color(myColor))
#                    print(*itemgetter(*faces)(vertex_coords))
            return cuboid
        
        a=2
        ul=cubeAll.get_corner(UL)
        dl=cubeAll.get_corner(DL)
        ur=cubeAll.get_corner(UR)
        abTop=ul+RIGHT*a
        abLeft=ul+DOWN*a
        abRight=ur+DOWN*a
        abBottom=dl+RIGHT*a

        aBrTop=Brace(Line(ul,abTop),UP)
        aBrTopLabel=aBrTop.get_tex("a")
        bBrTop=Brace(Line(abTop,ur),UP)
        bBrTopLabel=bBrTop.get_tex("b")
        aBrLeft=Brace(Line(ul,abLeft),LEFT)
        aBrLeftLabel=aBrLeft.get_tex("a")
        bBrLeft=Brace(Line(abLeft,dl),LEFT)
        bBrLeftLabel=bBrLeft.get_tex("b")

        aSq=Cuboid(2,2,2,myColor=YELLOW).align_to(cubeAll,UL+OUT)
        bSq=Cuboid(3,3,3,myColor=PURE_RED).align_to(cubeAll,DR+IN)
        labelA=MathTex("a^2").move_to(aSq.get_center())
        labelB=MathTex("b^2").move_to(bSq.get_center())
        # cubeA=Cube(2,fill_opacity=0.7,fill_color=YELLOW).align_to(cubeAll,UL+OUT)
        # cubeB=Cube(3,fill_opacity=0.7,fill_color=PURE_RED).align_to(cubeAll,DR+IN)

        # minimize prespective effect
        # so that view from the top, the cubes are square like
        self.camera.set_focal_distance(10000)

        # initialize 3 cuboids a^2b
        aSqb=[]            
        aSqb.append(Cuboid(2,2,3,myColor=PURE_BLUE))
        aSqb.append(aSqb[0].copy().rotate(90*DEGREES,axis=X_AXIS).align_to(cubeAll,DL+OUT))
        aSqb.append(aSqb[0].copy().rotate(90*DEGREES,axis=Y_AXIS).align_to(cubeAll,UR+OUT))
        aSqb[0].align_to(cubeAll,UL+IN)
        # initialize 3 cuboids ab^2
        abSq=[]
        abSq.append(Cuboid(3,3,2,myColor=PURE_GREEN))
        abSq.append(abSq[0].copy().rotate(90*DEGREES,axis=X_AXIS).align_to(cubeAll,UR+IN))
        abSq.append(abSq[0].copy().rotate(90*DEGREES,axis=Y_AXIS).align_to(cubeAll,DL+IN))
        abSq[0].align_to(cubeAll,DR+OUT)

        ab1oL=MathTex("ab").move_to(abSq[1].get_center())
        ab2oL=MathTex("ab").move_to(abSq[2].get_center())

        aPlusbSqTex=MathTex("({{a}}+{{b}})\\times({{a}}+{{b}})={{a^2}}+{{ab}}+{{ab}}+{{b^2}}").to_edge(UP)
        equalTex=MathTex("=").move_to(aPlusbSqTex[8][1].get_center())
        eq1=MathTex("(a+b)^2").next_to(equalTex,LEFT)
        eq2=MathTex("a^2").next_to(equalTex).set_color(YELLOW)
        eq3=MathTex("+").next_to(eq2)
        eq4=MathTex("2ab").next_to(eq3).set_color(PURE_GREEN)
        eq5=MathTex("+").next_to(eq4)
        eq6=MathTex("b^2").next_to(eq5).set_color(PURE_RED)

        finalTex=VGroup(eq1,eq2,eq3,eq4,eq5,eq6,equalTex)
        self.play(Write(finalTex))
        self.play(FadeIn(aSq,labelA))
        self.play(FadeIn(bSq,labelB))
        self.play(FadeIn(abSq[1],abSq[2],ab1oL,ab2oL))
        self.play(FadeIn(
            aBrTop,aBrTopLabel,bBrTop,bBrTopLabel,
            aBrLeft,aBrLeftLabel,bBrLeft,bBrLeftLabel)
        )
        self.wait(3)

        a2bLabel=[]
        for a2b in aSqb:
            a2bLabel.append(MathTex("a^2b").move_to(a2b.get_center()))
        ab2Label=[]
        for ab2 in abSq:
            ab2Label.append(MathTex("ab^2").move_to(ab2.get_center()))
        
#        map(lambda cLabel, cuboid: cLabel.add_updater(lambda mob: mob.move_to(cuboid.get_center())), a2bLabel, aSqb) 
#        map(lambda cLabel, cuboid: cLabel.add_updater(lambda mob: mob.move_to(cuboid.get_center())), ab2Label, abSq) 

        a2bLabel[0].add_updater(lambda mob: mob.move_to(aSqb[0].get_center()))
        a2bLabel[1].add_updater(lambda mob: mob.move_to(aSqb[1].get_center()))
        a2bLabel[2].add_updater(lambda mob: mob.move_to(aSqb[2].get_center()))

        ab2Label[0].add_updater(lambda mob: mob.move_to(abSq[0].get_center()))
        ab2Label[1].add_updater(lambda mob: mob.move_to(abSq[1].get_center()))
        ab2Label[2].add_updater(lambda mob: mob.move_to(abSq[2].get_center()))

        identity=MathTex("{{(a+b)^3=}}{{a^3}}+3{{a^2b}}+3{{ab^2}}+{{b^3}}").to_edge(UP)
        self.play(TransformMatchingTex(finalTex,identity),runtime=2)
        self.play(FadeOut(aBrTop,aBrTopLabel,bBrTop,bBrTopLabel))
        self.play(FadeOut(aBrLeft,aBrLeftLabel,bBrLeft,bBrLeftLabel))
        self.play(ReplacementTransform(labelA,MathTex("a^3").move_to(labelA.get_center())))
        self.play(ReplacementTransform(labelB,MathTex("b^3").move_to(labelB.get_center())))
        self.play(
            Transform(ab1oL,ab2Label[1]),
            Transform(ab2oL,ab2Label[2])
        )
        self.wait(3)
        self.play(FadeIn(*ab2Label))
        self.play(FadeIn(*a2bLabel))
        self.play(FadeOut(ab1oL,ab2oL,ab2Label[1],ab2Label[2]))
    
#        self.play(FadeIn(*aSqb))
#        self.play(FadeIn(*abSq))
        self.add(*aSqb,*abSq,aSq,bSq)

        self.play(FadeOut(identity))

#        self.move_camera(-50*DEGREES,-160*DEGREES,runtime=5)
        # initial -50 degree away from z-axis
        # self.begin_ambient_camera_rotation(-50*DEGREES/3, about='phi')
        # self.wait(3)
        # self.stop_ambient_camera_rotation(about='phi')
        # #  rotation -160 degree away from x-axis
        # self.begin_ambient_camera_rotation(-160*DEGREES/3, about='theta')
        # self.wait(3)
        # self.stop_ambient_camera_rotation(about='theta')

        # initial -50 degree away from z-axis
        self.begin_ambient_camera_rotation(-50*DEGREES/6, about='phi')
        #  rotation -160 degree away from x-axis
        self.begin_ambient_camera_rotation(-160*DEGREES/6, about='theta')
        self.wait(3)
        self.stop_ambient_camera_rotation(about='phi')
        self.stop_ambient_camera_rotation(about='theta')

        zoom0=self.camera.get_zoom()
#            print(zoom0)
        # animate camera zoom out to half the original zoom
        d2o=distance_to_origin.get_value()
        print(d2o)
        self.play(distance_to_origin.animate.set_value(0.6),runtime=10)        

        self.begin_ambient_camera_rotation(360*DEGREES/15, about='theta')
#        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
#        oldTheta=theta.get_value()
#        i=1
        for a2b in aSqb:
            a2b.generate_target()
            a2b.target.shift(UP*6)
#            self.play(MoveToTarget(a2b),theta.animate.set_value(oldTheta-(i*30)*DEGREES),runtime=10.0)
            self.play(MoveToTarget(a2b,runtime=5))
#             i+=1

#        i=1
        for ab2 in abSq:
            ab2.generate_target()
            ab2.target.shift(DOWN*6)
#            self.play(MoveToTarget(ab2),theta.animate.set_value(oldTheta-(90+i*30)*DEGREES),runtime=10.0)
            self.play(MoveToTarget(ab2,runtime=5))
#            i+=1
        self.play(FadeIn(labelA,labelB))
        self.play(FadeIn(*ab2Label))
        self.play(FadeIn(*a2bLabel))
        self.stop_ambient_camera_rotation(about='theta')

        self.begin_ambient_camera_rotation(360*DEGREES/10, about='theta')
        self.wait(5)
        self.stop_ambient_camera_rotation(about='theta')

        self.wait(2)
        self.play(Write(identity[0]))
        a3=labelA.copy().set_color(YELLOW)
        self.play(ReplacementTransform(a3,identity[1].set_color(YELLOW)))
        self.play(Write(identity[2]))
        for a2bL in a2bLabel:
            self.play(ReplacementTransform(a2bL,identity[3].set_color(BLUE)))
        self.play(Write(identity[4]))
        for ab2L in ab2Label:
            self.play(ReplacementTransform(ab2L,identity[5].set_color(PURE_GREEN)))
        self.play(Write(identity[6]))
        b3=labelB.copy().set_color(PURE_RED)
        self.play(ReplacementTransform(b3,identity[7].set_color(PURE_RED)))

        self.wait(2)

        self.begin_ambient_camera_rotation(360*DEGREES/40, about='theta')
#        i=1
        for a2b in aSqb:
            a2b.generate_target()
            a2b.target.shift(DOWN*6)
#            self.play(MoveToTarget(a2b),theta.animate.set_value(oldTheta-(180+i*30)*DEGREES),runtime=5.0)
            self.play(MoveToTarget(a2b),runtime=5.0)
#            i+=1

#        i=1
        for ab2 in abSq:
            ab2.generate_target()
            ab2.target.shift(UP*6)
#            self.play(MoveToTarget(ab2),theta.animate.set_value(oldTheta-(270+i*30)*DEGREES),runtime=5.0)
            self.play(MoveToTarget(ab2),runtime=5.0)
#            i+=1

        self.play(FadeOut(ab2Label[0]))
        self.play(FadeOut(*a2bLabel))
#        self.wait(2)

        self.stop_ambient_camera_rotation(about='theta')
        # revert the initial -50 degree away from z-axis
        self.begin_ambient_camera_rotation(25*DEGREES/3, about='phi')
        self.wait(3)
        self.stop_ambient_camera_rotation(about='phi')
        #  rotation 90 degree about z-axis to correct the x-y plan having x as horizontal
#        self.begin_ambient_camera_rotation(-90*DEGREES/3, about='gamma')
#        self.wait(3)
#        self.stop_ambient_camera_rotation(about='gamma')
        # to be exact on the camera orientation right above the x-y plan
        self.move_camera(0*DEGREES,0*DEGREES,(90-360)*DEGREES)
#        self.camera.set_zoom(zoom0)
        self.play(distance_to_origin.animate.set_value(zoom0))        
        # self.add(labelA.set_color(WHITE))
        # self.add(labelB.set_color(WHITE))
        # self.play(FadeIn(ab2Label[1].set_color(WHITE),ab2Label[2].set_color(WHITE)))
#        self.play(FadeIn(ab2Label[2].set_color(WHITE)))
        self.wait(5)
        # self.move_camera(30*DEGREES, 90*DEGREES)
        # self.move_camera(55*DEGREES, 180*DEGREES)
#            self.camera.frame.add_updater(lambda mob, dt: mob.increment_theta(0.1 * dt))

#            self.play(Transform(cubeB,cubeA),runtime=3)

class test(Scene):
    def construct(self):
        a=MathTex("\sqrt{","{{(}}{{1}}{{)}}{{^2}}{{+}}{{(}}{{\\frac{\sqrt{5}-1}{2}}}{{)}}{{^2}}}")
        for i in a:
            print(i) 
#        b=MathTex("\sqrt{","{{(1)^2}}+{{(\\frac{\sqrt{5}-1}{2})^2}}")
        b=MathTex("\sqrt{","{{1}}^2+{{\\frac{1}{2}}}^2}")
        for i in b:
            print(i) 

#        print(b[1][1])
#        print(b[3][1:5])

        c=MathTex("{{1{{2}}3}}{{4{{{{{5.1}{5.2}}}{{6}}}}7}}")
        previous=Dot().to_edge(UP)
        # for i in c:
        #     print(i)
           
        #     for j in i.submobjects:
        #         print(j)
        #         self.add(j.next_to(previous,DOWN)) 
        #         self.add(index_labels(j))
        #         previous=j

#        self.add(index_labels(c))

        self.add(b,index_labels(b),index_labels(b[1]),index_labels(b[3]))


        return super().construct()


class abc(Scene):
    def construct(self):

        aPlusb=5       
        bigS=Square(aPlusb).to_edge(DOWN)

        self.add(bigS)

        a=bigS.side_length*3/aPlusb
        b=bigS.side_length-a

        ul=bigS.get_corner(UL)
        dl=bigS.get_corner(DL)
        ur=bigS.get_corner(UR)
        dr=bigS.get_corner(DR)
        abTop=ul+RIGHT*a
        abLeft=ul+DOWN*a
        abRight=ur+DOWN*a
        abBottom=dl+RIGHT*a
        cross=abTop+DOWN*a

        aBrTop=Brace(Line(ul,abTop),UP)
        aBrTopLabel=aBrTop.get_tex("a")
        bBrTop=Brace(Line(abTop,ur),UP)
        bBrTopLabel=bBrTop.get_tex("b")
        aBrLeft=Brace(Line(ul,abLeft),LEFT)
        aBrLeftLabel=aBrLeft.get_tex("a")
        bBrLeft=Brace(Line(abLeft,dl),LEFT)
        bBrLeftLabel=bBrLeft.get_tex("b")
        self.play(FadeIn(aBrTop,aBrTopLabel,bBrTop,bBrTopLabel))
        self.play(FadeIn(aBrLeft,aBrLeftLabel,bBrLeft,bBrLeftLabel))

        L1=Line(abTop,abBottom)
        L2=Line(abLeft,abRight)
        self.play(Write(L1))
        self.play(Write(L2))
        aSq=Square(a,color=YELLOW).set_opacity(0.7).align_to(bigS,UL).set_stroke(None)

        a1=aBrTopLabel.copy()
        a1.generate_target()
        a1.target.move_to(aSq.get_center())
        a2=aBrLeftLabel.copy()
        a2.generate_target()
        a2.target.move_to(aSq.get_center())

        self.play(MoveToTarget(a1),MoveToTarget(a2))
        aSqTex=MathTex("a^2").move_to(aSq.get_center())
        self.play(FadeOut(a1,a2),FadeIn(aSqTex))
        self.play(FadeIn(aSq))

        bSq=Square(b,color=PURE_RED).set_opacity(0.7).align_to(bigS,DR).set_stroke(None)
        b1=bBrTopLabel.copy()
        b1.generate_target()
        b1.target.move_to(bSq.get_center())
        b2=bBrLeftLabel.copy()
        b2.generate_target()
        b2.target.move_to(bSq.get_center())

        self.play(MoveToTarget(b1),MoveToTarget(b2))
        bSqTex=MathTex("b^2").move_to(bSq.get_center())
        self.play(FadeOut(b1,b2),FadeIn(bSqTex))
        self.play(FadeIn(bSq))

        t1=Polygon(cross,abTop,ur,color=PURE_GREEN).set_opacity(0.7).align_to(bigS,UR)
        t2=Polygon(cross,abRight,ur,color=PURE_GREEN).set_opacity(0.7).align_to(bigS,UR)
        t3=Polygon(abLeft,cross,abBottom,color=PURE_GREEN).set_opacity(0.7).align_to(bigS,DL)
        t4=Polygon(abBottom,dl,abLeft,color=PURE_GREEN).set_opacity(0.7).align_to(bigS,DL)

        self.play(FadeIn(t1))
        self.play(FadeIn(t2))
        self.play(FadeIn(t3))
        self.play(FadeIn(t4))

        abRect=VGroup(t1,t2)
        baRect=VGroup(t3,t4)

        Asq=VGroup(aSq,aSqTex)
        Bsq=VGroup(bSq,bSqTex)

        Asq.generate_target()
        Asq.target.to_edge(LEFT)
        Bsq.generate_target()
        Bsq.target.to_edge(LEFT)

        self.play(MoveToTarget(Asq),MoveToTarget(Bsq))

        self.play(Rotate(t3,angle=-PI/2,about_point=abBottom,rate_functions=linear))
        abRect.generate_target()
        abRect.target.align_to(bigS,UL)
        self.play(MoveToTarget(abRect))

        baTop=ul+RIGHT*b
        baRight=ur+DOWN*b

        BBrTop=Brace(Line(ul,baTop),UP)
        BBrTopLabel=BBrTop.get_tex("b")

        ABrTop=Brace(Line(baTop,ur),UP)
        ABrTopLabel=ABrTop.get_tex("a")

        self.play(FadeOut(L1,L2))

        self.play(
            ReplacementTransform(aBrTop,BBrTop),
            ReplacementTransform(aBrTopLabel,BBrTopLabel),
            ReplacementTransform(bBrTop,ABrTop),
            ReplacementTransform(bBrTopLabel,ABrTopLabel)
        )

        self.play(Rotate(t2,angle=PI/2,about_point=baTop,rate_functions=linear))

        lineC=Line(abLeft,baTop)
        cBr=Brace(lineC,direction=lineC.copy().rotate(-PI / 2).get_unit_vector(),buff=0.0)
        cBrLabel=cBr.get_tex("c")

        self.play(FadeIn(cBr,cBrLabel))


        cSq=Polygon(baTop,baRight,abBottom,abLeft,color=PURE_BLUE).set_opacity(0.7)
        cSqTex=MathTex("c^2").move_to(cSq.get_center())

        self.play(FadeIn(cSq,cSqTex),runtime=3)


        Asq.generate_target()
        Asq.target.next_to(bigS,LEFT,buff=0.0).align_to(bigS,UP)
        Bsq.generate_target()
        Bsq.target.next_to(bigS,UP,buff=0.0).align_to(bigS,LEFT)

        self.play(FadeOut(bBrLeft,bBrLeftLabel,ABrTop,ABrTopLabel),runtime=2)

        self.play(MoveToTarget(Asq),MoveToTarget(Bsq),runtime=2)

        self.play(
            FadeOut(aBrLeft,aBrLeftLabel,BBrTop,BBrTopLabel,cBr,cBrLabel),
            FadeOut(bigS),
            runtime=2.0
        )

        dim=ValueTracker(0.7)
        t2.add_updater(lambda mob: mob.set_opacity(dim.get_value()))
        t3.add_updater(lambda mob: mob.set_opacity(dim.get_value()))
        t4.add_updater(lambda mob: mob.set_opacity(dim.get_value()))
        self.play(
            dim.animate.set_value(0.2),
            runtime=3.0, rate_func=linear
        )

        title1=MathTex("Pythagorean\ theorem").to_corner(UR)
        title2=MathTex("a^2+b^2=c^2").next_to(title1,DOWN)
        self.play(Write(title1))
        self.play(Write(title2))
        self.wait(2)

        a=ValueTracker(bigS.side_length*3/aPlusb)
        cSq.add_updater(lambda mob: mob.become(Polygon(
                                                ul+RIGHT*(bigS.side_length-a.get_value()),
                                                ur+DOWN*(bigS.side_length-a.get_value()),
                                                dl+RIGHT*a.get_value(),
                                                ul+DOWN*a.get_value(),
                                                color=PURE_BLUE).set_opacity(0.7))) 
        cSqTex.add_updater(lambda mob: mob.move_to(cSq.get_center()))
        bSq.add_updater(lambda mob: mob.become(Square(bigS.side_length-a.get_value(),color=PURE_RED).set_opacity(0.7).next_to(bigS,UP,buff=0.0).align_to(bigS,LEFT)))
        aSq.add_updater(lambda mob: mob.become(Square(a.get_value(),color=YELLOW).set_opacity(0.7).next_to(bigS,LEFT,buff=0.0).align_to(bigS,UP)))
        bSqTex.add_updater(lambda mob: mob.move_to(bSq.get_center()))
        aSqTex.add_updater(lambda mob: mob.move_to(aSq.get_center()))

        t2.clear_updaters()
        t3.clear_updaters()
        t4.clear_updaters()
        t1.add_updater(lambda mob: mob.become(Polygon(ul,ur+LEFT*a.get_value(),ul+DOWN*a.get_value(),color=PURE_GREEN).set_opacity(0.7))) 
        t2.add_updater(lambda mob: mob.become(Polygon(dr+UP*a.get_value(),ur,ur+LEFT*a.get_value(),color=PURE_GREEN).set_opacity(0.2)))
        t3.add_updater(lambda mob: mob.become(Polygon(dr+UP*a.get_value(),dr,dl+RIGHT*a.get_value(),color=PURE_GREEN).set_opacity(0.2)))
        t4.add_updater(lambda mob: mob.become(Polygon(ul+DOWN*a.get_value(),dl,dl+RIGHT*a.get_value(),color=PURE_GREEN).set_opacity(0.2)))

        self.play(a.animate.set_value(bigS.side_length*5/aPlusb),runtime=3,rate_func=linear)
        self.play(a.animate.set_value(bigS.side_length*2.5/aPlusb),runtime=3,rate_func=linear)
        self.play(Write(MathTex("true\ for\ all\ right\ angle\ triangles").next_to(title2,DOWN).scale(0.7)),runtime=2)
        self.play(a.animate.set_value(bigS.side_length*5/aPlusb),runtime=3,rate_func=linear)
        self.play(a.animate.set_value(bigS.side_length*3/aPlusb),runtime=3,rate_func=linear)
        self.wait(3)

class pascalTriangle(ThreeDScene):
    def construct(self):
        tt=MathTex("Pascal\ Triangle\ and\ Coefficient\ of\ Binomial\ Expansion")    
        self.play(Write(tt))
        self.wait(5)
        self.play(FadeOut(tt))

        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        #intro    
        line=[]
        line.append(MathTex("{{(a+b)^0}}={{1}}"))
        line.append(MathTex("{{(a+b)^1}}={{a+b}}"))
        line.append(MathTex("{{(a+b)^2}}={{a^2+2ab+b^2}}"))
        line.append(MathTex("{{(a+b)^3}}={{a^3+3a^2b+3ab^2+b^3}}"))
        line.append(MathTex("{{(a+b)^4}}={{a^4+4a^3b++6a^2b^2+4ab^3+b^3}}"))
        line.append(MathTex("{{(a+b)^n}}={{\sum_{k=0}^{n}\\binom{n}{k}a^{n-k}b^k}}"))

        self.play(Write(line[0].to_edge(UL)))
        for i in range(1,len(line)):
            line[i].next_to(line[i-1],DOWN).align_to(line[i-1],LEFT)
            self.play(ReplacementTransform(line[i-1][0].copy(),line[i][0]),ReplacementTransform(line[i-1][2].copy(),line[i][2]),FadeIn(line[i][1]),run_time=2)

        nCr=MathTex("\\binom{n}{r}=\\frac{n!}{k!(n-k)!}")
        self.play(Write(nCr.next_to(line[-1],DOWN).align_to(line[-1],LEFT)))
        for i in range(len(line)-1):
            line[i][2].generate_target()
            line[i][2].target.set_x(x=0,direction=ORIGIN)
            self.play(MoveToTarget(line[i][2]),run_time=2)

        self.play(FadeOut(nCr))
        self.play(FadeOut(line[-1]))
        self.wait(2)

        #fade out equal sign
        self.play(FadeOut(*list(map(lambda item: item[1], line[:-1]))))
        # fade out left hand side
        self.play(FadeOut(*list(map(lambda item: item[0], line[:-1]))))
        # fade out right hand side, 4 lines triangle
        self.wait(3)
        self.play(FadeOut(*list(map(lambda item: item[2], line[:-1]))))

        # draw Pascal Triangle
        class Node(Square):
            def __init__(self, value, n, r, **kwargs):
                side_length=0.5
                super().__init__(side_length, **kwargs)
                self.set_opacity(0).set_stroke(YELLOW,width=3).set_opacity(0.3).set_color(YELLOW)
                self.value=value
                self.tex=MathTex(value)
                self.n = n
                self.r = r
                self.tex.add_updater(lambda mob: mob.move_to(self))
                if (self.tex.width) > side_length*1.5:
                    texScale = side_length/self.tex.width*1.5
                else:
                    texScale = 1.0
                self.tex.scale(texScale)

        pTree=VGroup()

        a=Node(1,0,0)
        pTree.add(a)
        a.to_edge(UP)
#        self.play(FadeIn(a,a.tex))
        def genNextLevel(cLevel):
            nLevel=[]
            thisNode=Node(1,cLevel[0].n+1,0).move_to(cLevel[0].get_center()+(DOWN+LEFT)*a.side_length)
            nLevel.append(thisNode)
            pTree.add(thisNode)
            cLen=len(cLevel)
            if (cLen > 1):
                for i in range(cLen-1):
                    # to do
                    thisNode=Node(cLevel[i].value+cLevel[i+1].value,cLevel[0].n+1,i+1).move_to((cLevel[i].get_center()+cLevel[i+1].get_center())/2 + DOWN*a.side_length)
                    nLevel.append(thisNode)
                    pTree.add(thisNode)
            thisNode=Node(1,cLevel[0].n+1,cLevel[0].n+1).move_to(cLevel[-1].get_center()+(DOWN+RIGHT)*a.side_length)
            nLevel.append(thisNode)
            pTree.add(thisNode)

            fullLength=len(nLevel)
            halfWay=math.ceil(fullLength/2)
            if fullLength<=12: # symetrically 1 by 1
                self.play(
                    ReplacementTransform(cLevel[ 0].tex.copy(),nLevel[ 0].tex),
                    ReplacementTransform(cLevel[-1].tex.copy(),nLevel[-1].tex)
                )
                if fullLength > 2:
                    for i in range(1,halfWay-1):
    #                self.play(FadeIn(nLevel[i],nLevel[-1*i-1],nLevel[i].tex,nLevel[-1*i-1].tex))
                        self.play(
                            ReplacementTransform(cLevel[i-1].tex.copy(),nLevel[i].tex),
                            ReplacementTransform(cLevel[i].tex.copy(),nLevel[i].tex),
                            ReplacementTransform(cLevel[-1*i  ].tex.copy(),nLevel[-1*i-1].tex),
                            ReplacementTransform(cLevel[-1*i-1].tex.copy(),nLevel[-1*i-1].tex)
                        )   
                    if (fullLength % 2 == 1):
                    #                self.play(FadeIn(nLevel[halfWay-1],nLevel[halfWay-1].tex))
                        self.play(
                            ReplacementTransform(cLevel[halfWay-2].tex.copy(),nLevel[halfWay-1].tex),
                            ReplacementTransform(cLevel[halfWay-1].tex.copy(),nLevel[halfWay-1].tex)
                        )
                    else:
        #                self.play(FadeIn(nLevel[halfWay-1],nLevel[halfWay],nLevel[halfWay-1].tex,nLevel[halfWay].tex))
                        self.play(
                            ReplacementTransform(cLevel[halfWay-2].tex.copy(),nLevel[halfWay-1].tex),
                            ReplacementTransform(cLevel[halfWay-1].tex.copy(),nLevel[halfWay-1].tex),
                            ReplacementTransform(cLevel[halfWay-1].tex.copy(),nLevel[halfWay].tex),
                            ReplacementTransform(cLevel[halfWay  ].tex.copy(),nLevel[halfWay].tex)
                        )
            else: # whole level in parallel
                actions=[]
                actions.append(ReplacementTransform(cLevel[ 0].tex.copy(),nLevel[ 0].tex))
                actions.append(ReplacementTransform(cLevel[-1].tex.copy(),nLevel[-1].tex)) 
                for i in range(1,fullLength-1):
                    actions.append(ReplacementTransform(cLevel[i-1].tex.copy(),nLevel[i].tex))
                    actions.append(ReplacementTransform(cLevel[i  ].tex.copy(),nLevel[i].tex))
                self.play(*actions,runtime=3)
            return nLevel 

        currentLevel=[a]
        self.play(FadeIn(a.tex))
        for i in range(12): #12
            nextLevel=genNextLevel(currentLevel)
            currentLevel=nextLevel
        self.play(distance_to_origin.animate.set_value(0.72))
        self.move_camera(frame_center=np.array([0.0,-2.0,1.0]))
        for i in range(8): #8
            nextLevel=genNextLevel(currentLevel)
            currentLevel=nextLevel

        counter=MathTex("nCr=\\binom{n}{r}=\\frac{n!}{k!(n-k)!}").to_edge(UL).shift(LEFT*3)
        self.play(FadeIn(counter))
        self.wait(2)
        for mob in pTree.submobjects:
            self.add(mob)
            self.wait(2/(mob.n+1))
            counter.become(MathTex(
                    "_{"+str(mob.n)+"}C_{"+str(mob.r)+"}=\\binom{" + str(mob.n) + "}{" + str(mob.r) + 
                    "}=\\frac{"+str(mob.n)+"!}{"+str(mob.r)+"!"+str(mob.n-mob.r)+"!}="+str(mob.value)).to_edge(UL).shift(LEFT*3).set_color(YELLOW))
            self.remove(mob)
        self.wait(5)

            

class drawHexgon(Scene):
    def construct(self):
        origin=Dot(radius=0.04)
        self.add(origin)
        centre=Dot(color=RED,radius=0.04)
        self.play(FadeIn(centre))

        c = Circle(2).set_stroke(width=2).set_color(YELLOW)
        self.play(Write(c))

        num_points = 6
        # Calculate each angle
        angles = [n * (360 / num_points) for n in range(num_points)]
        # Points on circumference of circle
        points = [c.point_at_angle(n*DEGREES) for n in angles]
        colourList = color_gradient([PURE_RED,ORANGE,YELLOW,PURE_GREEN,PURE_BLUE,LIGHT_PINK],len(points))

        d=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,colourList)]

        def mCircleFadeOutIn(mob:Circle):
            theta=np.arctan(mob.get_y()/mob.get_x())
            mob.set_stroke(opacity=0.3+0.7*(1-abs(np.sin(theta*3))))

        movingCircle = c.copy().set_color(ORANGE)
        movingCircle.add_updater(lambda mob: mob.move_to(centre))
        movingCircle.add_updater(mCircleFadeOutIn)

        self.add(movingCircle)

        self.play(ReplacementTransform(centre,d[0]))
        self.add(d[5])

        for dd in d[:-2]:
            self.add(dd)
            self.play(
                Write(Line(centre,dd,color=dd.color),
                run_time=2,
                rate_func=linear)
            )
            self.play(
                Transform(
                    centre,
                    dd,
                    path_func=utils.paths.path_along_arc(TAU * 1 / 6),
                    run_time=3,
                    rate_func=linear)
            )

        movingCircle.clear_updaters()
        for dd in [*d[4:],d[0]]:
            self.play(FadeIn(dd))
            self.play(
                Write(Line(centre,dd,color=dd.color,buff=0))
            )
            centre.move_to(dd)

        self.play(FadeOut(movingCircle))
        self.play(FadeOut(c))
        self.play(FadeOut(origin,centre))
        self.play(FadeIn(Polygon(*points).set_color(WHITE).set_opacity(0.7)),runtime=5)


class drawPentagon(Scene):
    def construct(self):
        self.play(Write(Title("Draw Regular Pentagon with straight ruler and compass").scale(0.8)))
        c = Circle(2).set_stroke(width=2).set_stroke(PURE_RED,opacity=0.5)
        self.play(Write(c))

        num_points = 5
        # Calculate each angle
        angles = [(n * (360 / num_points) +90) % 360 for n in range(num_points)]
        # Points on circumference of circle
        # First point at the top
        points = [c.point_at_angle(n*DEGREES) for n in angles]
        colourList = color_gradient([PURE_RED,ORANGE,YELLOW,PURE_GREEN,PURE_BLUE,LIGHT_PINK],len(points))

        d=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,colourList)]

        origin=Dot(radius=0.04)
        self.add(origin)

#        traceDot=TracedPath(centre.get_center)
#        self.add(traceDot)

        leftDot=Dot(LEFT*2, color=PURE_GREEN,radius=0.04)
        rightDot=Dot(RIGHT*2, color=PURE_GREEN,radius=0.04)
        self.add(leftDot)
        lineH=Line(leftDot,rightDot)
        self.play(Write(lineH))
        self.add(rightDot)
        leftCircle=Circle(2.1).set_stroke(width=2).set_color(PURE_GREEN).move_to(LEFT*2)
        rightCircle=Circle(2.1).set_stroke(width=2).set_color(PURE_GREEN).move_to(RIGHT*2)
        # 1st bisector
        self.play(GrowFromPoint(leftCircle,leftDot),GrowFromPoint(rightCircle,rightDot))
        lineB1=Line(UP*3,DOWN*3)
        self.play(Write(lineB1))
        self.play(FadeOut(leftCircle,rightCircle))
        br1=Brace(Line(d[0],origin),LEFT)
        br1Label=MathTex("1").next_to(br1,LEFT)
        self.play(FadeIn(br1,br1Label))

        # 2nd bisector
        cCircle=Circle(1.1).set_stroke(width=2).set_color(PURE_GREEN)
        rCircle=Circle(1.1).set_stroke(width=2).set_color(PURE_GREEN).move_to(RIGHT*2)
        self.play(GrowFromPoint(cCircle,origin),GrowFromPoint(rCircle,rightDot))
        lineB2=Line(UP*2.5 + RIGHT, DOWN*2.5 + RIGHT)
        self.play(Write(lineB2))
        self.play(FadeOut(cCircle,rCircle))
        brHalf1=Brace(Line(origin,RIGHT),DOWN,buff=0.0)
        brHalf1Label=MathTex("\\frac{1}{2}").next_to(brHalf1,DOWN,buff=0).scale(0.5)
        brHalf2=Brace(Line(RIGHT,RIGHT*2),DOWN,buff=0.0)
        brHalf2Label=MathTex("\\frac{1}{2}").next_to(brHalf2,DOWN,buff=0).scale(0.5)
        self.play(FadeIn(brHalf1,brHalf1Label,brHalf2,brHalf2Label))

        line1=Line(RIGHT,d[0]).set_color(PURE_GREEN)
        self.play(Write(line1))
        offset1=0.7
        norm1=line1.copy().rotate(- PI / 2,about_point=line1.get_center()).get_unit_vector()*offset1

        br5=Brace(line1,direction=norm1)
        br5Label=br5.get_tex("\sqrt{","{{1}}^2+{{\\frac{1}{2}}}^2}").scale(0.5).set_color(PURE_GREEN).move_to(br5.get_center()+line1.copy().rotate(- PI / 2,about_point=line1.get_center()).get_unit_vector()*offset1)
        self.add(br5)

        h=br1Label.copy()
        self.play(ReplacementTransform(h,br5Label[1][0]))
        self.wait()
        self.play(FadeIn(br5Label[2][0]))
        self.wait()
        hh=brHalf1Label.copy()
        self.play(ReplacementTransform(hh,br5Label[3]))
        self.wait()
        self.play(FadeIn(br5Label[4]))
        self.wait()
        self.play(FadeIn(br5Label[0],br5Label[2][1]))
        self.wait()

#        hGroup=VGroup(h,hh)

        br5texStrings=[
#                        "\sqrt{1^2+\\frac{1}{2}^2}",
                        "\sqrt{\\frac{4}{4}+\\frac{1}{4}}",
                        "\sqrt{\\frac{5}{4}",
                        "\\frac{\sqrt{5}}{2}"
        ]

        formulaTransitionTime=2

        br5texLs=[]
        for ts in br5texStrings:
            br5texLs.append(MathTex(ts).scale(0.5).set_color(PURE_GREEN).move_to(br5.get_center()+norm1))

        for br5texL in br5texLs:
            self.play(ReplacementTransform(br5Label,br5texL))
#            self.play(TransformMatchingTex(br5Label,br5texL))
            br5Label=br5texL
            self.wait(formulaTransitionTime)

        br5Label.add_updater(lambda mob: mob.move_to(br5.get_center()+line1.copy().rotate(- PI / 2,about_point=line1.get_center()).get_unit_vector()*offset1))
        br5.add_updater(lambda mob: mob.become(Brace(line1,direction=line1.copy().rotate(- PI / 2,about_point=line1.get_center()).get_unit_vector()*offset1))) 

        dCircle=Circle(np.sqrt(5)).set_stroke(width=2).set_color(PURE_GREEN).move_to(RIGHT)
        self.play(GrowFromPoint(dCircle,RIGHT))

        self.play(FadeOut(br1,br1Label))
        self.play(FadeOut(brHalf2,brHalf2Label))

        eDot=Dot(LEFT*(np.sqrt(5)-1), color=PURE_BLUE,radius=0.04)
        m1=d[0].copy()
        line1.add_updater(lambda mob:  mob.become(Line(RIGHT,m1).set_color(PURE_GREEN)))

        self.play(
            Transform(
                m1,
                eDot,
                path_func=utils.paths.path_along_arc(TAU * 1 / 6),
#                path_along_arc=utils.paths.path_along_circles(2 * PI,RIGHT),
                run_time=1,
                rate_func=linear)
        )

        eCircle=Circle(np.sqrt((5-np.sqrt(5))/2)*2).set_stroke(width=2).set_color(YELLOW).move_to(d[0])
        self.add(eDot)
        self.play(FadeOut(dCircle))
        self.play(FadeOut(lineB2))

        br5m1=Brace(Line(origin,eDot),DOWN,buff=0.0)
        br5m1Label=br5m1.get_tex("\\frac{\sqrt{5}}{2}-\\frac{1}{2}").scale(0.5).set_color(PURE_GREEN).shift(UP*0.5)
        self.play(FadeIn(br5m1,br5m1Label))
        self.wait()
        self.play(FadeOut(brHalf1,brHalf1Label))
        self.wait()
        self.play(FadeOut(br5,br5Label))
        self.wait()
        self.play(Transform(br5m1Label,MathTex("\\frac{\sqrt{5}-1}{2}").scale(0.5).set_color(PURE_GREEN).move_to(br5m1Label.get_center())),runtime=2.0)
        self.wait()
        br1.become(Brace(Line(d[0],origin),RIGHT))
        br1Label.next_to(br1,RIGHT)
        self.play(FadeIn(br1,br1Label))

        line2=Line(d[0],eDot).set_color(YELLOW)
        self.play(FadeIn(d[0]))
        self.play(Write(line2))

        offset2=1.1
        norm2=line2.copy().rotate(-PI / 2,about_point=line2.get_center()).get_unit_vector()*offset2
        brEdge=Brace(line2,direction=norm2)
        brEdgeLabel=brEdge.get_tex("\sqrt{","{{(1)^2}}+{{(\\frac{\sqrt{5}-1}{2})^2}}").scale(0.5).set_color(YELLOW).move_to(brEdge.get_center()+norm2)
        brEdge.add_updater(lambda mob: mob.become(Brace(line2,direction=line2.copy().rotate(-PI / 2,about_point=line2.get_center()).get_unit_vector())))
        self.play(FadeIn(brEdge))

        self.play(ReplacementTransform(br1Label,brEdgeLabel[1][1]))
        self.wait()
        self.play(FadeIn(brEdgeLabel[1][0],brEdgeLabel[1][2],brEdgeLabel[1][3]))
        self.play(FadeOut(br1))
        self.play(ReplacementTransform(br5m1Label,brEdgeLabel[3][1:8]))
        self.wait()
        self.play(FadeIn(brEdgeLabel[3][0],brEdgeLabel[3][0],brEdgeLabel[3][8:10]))
        self.play(FadeOut(br5m1))
        self.play(FadeIn(brEdgeLabel[0],brEdgeLabel[2]))
        self.wait(formulaTransitionTime)

        norm2=line2.copy().rotate(-PI / 2,about_point=line2.get_center()).get_unit_vector()*offset2

        texStrings=[
                    "\sqrt{1^2+\\frac{(\sqrt{5}-1)^2}{2^2}}",
                    "\sqrt{1+\\frac{\sqrt{5}^2+1-2\sqrt{5}}{4}}",
                    "\sqrt{\\frac{4}{4}+\\frac{5+1-2\sqrt{5}}{4}}",
                    "\sqrt{\\frac{4+5+1-2\sqrt{5}}{4}}",
                    "\sqrt{\\frac{10-2\sqrt{5}}{4}}",
                    "\sqrt{\\frac{5-\sqrt{5}}{2}}"
        ]
        brELs=[]
        for ts in texStrings:
            brELs.append(MathTex(ts).scale(0.5).set_color(YELLOW).move_to(brEdge.get_center()+norm2))

        for brEL in brELs:
            self.play(ReplacementTransform(brEdgeLabel,brEL))
#            self.play(TransformMatchingTex(brEdgeLabel,brEL))
            brEdgeLabel=brEL
            self.wait(formulaTransitionTime)

        brEdgeLabel.add_updater(lambda mob: mob.move_to(brEdge.get_center()+line2.copy().rotate(-PI / 2,about_point=line2.get_center()).get_unit_vector()*offset2))

        m2=eDot.copy()
        line2.add_updater(lambda mob:  mob.become(Line(d[0],m2).set_color(YELLOW)))

        self.play(GrowFromPoint(eCircle,d[0]))

        self.play(
            Transform(
                m2,
                d[1],
                path_along_arc=utils.paths.path_along_circles(2 * PI,d[0].get_center()),
                run_time=1,
                rate_func=linear)
        )

        def mCircleFadeOutIn(mob:Circle):
            theta=np.arctan(mob.get_y()/mob.get_x())
            mob.set_stroke(opacity=0.3+0.7*(1-abs(np.sin(theta*num_points/2))))

        centre=Dot(color=PURE_RED,radius=0.04).move_to(d[0])
        self.play(FadeIn(centre))
        for mob in (m1, eDot, line1, lineB1, lineH, rightDot, leftDot, brEdge, brEdgeLabel):
            self.play(FadeOut(mob))

        movingCircle = eCircle
        movingCircle.add_updater(lambda mob: mob.move_to(centre))
        movingCircle.add_updater(mCircleFadeOutIn)

        self.add(d[0])
#        self.add(movingCircle)
        for dd in d[1:-1]:
            self.add(dd)
            self.play(
                Write(Line(centre,dd,color=dd.color),
                run_time=2,
                rate_func=linear)
            )
            self.play(
                Transform(
                    centre,
                    dd,
#                    path_func=utils.paths.path_along_arc(TAU * 1 / 6),
                    run_time=2,
                    rate_func=linear)
            )

        self.add(d[-1])
        self.play(FadeOut(eCircle))
        self.play(Write(Line(d[-2],d[-1]).set_color(d[-1].get_color())))
        self.play(Write(Line(d[-1],d[0]).set_color(d[0].get_color())))
# #        movingCircle.clear_updaters()
#         for dd in [*d[4:],d[0]]:
#             self.play(FadeIn(dd))
#             self.play(
#                 Write(Line(centre,dd,color=dd.color,buff=0))
#             )
#             centre.move_to(dd)

#        self.play(FadeOut(movingCircle))
#        self.play(FadeOut(c))
        self.play(FadeOut(origin,centre, c))
        self.play(FadeIn(Polygon(*points).set_fill(YELLOW,opacity=1).set_stroke(YELLOW,opacity=0)))


class perpendicularBisector(Scene):
    def construct(self):
        axes = NumberPlane().set_opacity(0.2)
        self.add(axes)

        t=Title("Perpendicular Bisector of an arbitrary line segment")

        self.play(Write(t))
        d1=Dot(np.array([-3.4,-2.6,0.0]),radius=0.05).set_opacity(0.0)
        d2=d1.copy()

        d2.generate_target()
        d2.target.move_to(np.array([3.7,3.2,0.0]))
        
        line=Line(d1,d2)
        self.add(line)
        line.add_updater(lambda mob: mob.become(Line(d1,d2)))

        self.add(d1,d2)
        self.play(MoveToTarget(d2))

        d2.generate_target()
        d2.target.move_to(np.array([-2.6,-0.8,0.0]))
        d1.generate_target()
        d1.target.move_to(np.array([1.6,1.4,0.0]))

        self.play(MoveToTarget(d1),MoveToTarget(d2),run_time=4)

        r = np.sqrt((d1.get_x() - d2.get_x()) * (d1.get_x() - d2.get_x()) + (d1.get_y() - d2.get_y()) * (d1.get_y() - d2.get_y()))/2 * 1.1  
        c1=Circle(r).move_to(d1)
        c2=Circle(r).move_to(d2)

        self.play(GrowFromPoint(c1,d1),GrowFromPoint(c2,d2))

        pline=Line(d1,d2).rotate(90*DEGREES,about_point=line.get_center()).set_color(YELLOW).scale(0.6)
        self.play(Create(pline))
        self.play(FadeIn(RightAngle(line,pline)),run_time=3)
        self.play(FadeOut(c1,c2),run_time=5)

        self.wait(5)

class angleBisector(Scene):
    def construct(self):
        axes = NumberPlane().set_opacity(0.2)
        self.add(axes)

        t=Title("Angle Bisector of an arbitrary angle")
        self.play(Write(t))
        r=3
        c0=Circle(r).set_opacity(0.0)
        theta=ValueTracker(0.01)

        d1=Dot(np.array([r,0,0]),radius=0.05).set_opacity(0.0)
        d2=d1.copy().move_to(c0.point_at_angle(theta.get_value()))
        d2.add_updater(lambda mob: mob.move_to(c0.point_at_angle(theta.get_value())))

        line1=Line(ORIGIN,d1)
        line2=Line(ORIGIN,d2)
        self.add(line1,line2)
        line2.add_updater(lambda mob: mob.become(Line(ORIGIN,c0.point_at_angle(theta.get_value()))))

        angle=Angle(line1,line2,radius=0.3)
        angle.add_updater(lambda mob: mob.become(Angle(line1,line2,radius=0.3)))
        self.add(angle)

        # damp to 70 degree
        self.play(theta.animate.set_value(130*DEGREES), run_time=3.0)
        self.play(theta.animate.set_value( 40*DEGREES), run_time=2.0)
        self.play(theta.animate.set_value( 80*DEGREES), run_time=1.5)
        self.play(theta.animate.set_value( 70*DEGREES), run_time=1.0)

        c1=Circle(2)

        self.play(GrowFromCenter(c1),run_time=2)
        md2=Dot(c1.point_at_angle(0)).set_color(YELLOW).scale(0.5)
        md3=Dot(c1.point_at_angle(theta.get_value())).set_color(YELLOW).scale(0.5)
        md3.add_updater(lambda mob: mob.move_to(c1.point_at_angle(theta.get_value())))
        c2=Circle(1.3).move_to(md2).set_color(YELLOW)
        c3=Circle(1.3).move_to(md3).set_color(YELLOW)
        self.play(FadeIn(md2,md3))
        self.play(FadeOut(c1),run_time=2)
        self.play(GrowFromCenter(c2),GrowFromCenter(c3),run_time=3)
        bisector=line1.copy().rotate(theta.get_value()/2,about_point=ORIGIN).set_color(PURE_GREEN)
        self.play(Write(bisector),run_time=2)

        def distance(d1: Dot, d2: Dot) -> float:
            return np.sqrt((d1.get_x() - d2.get_x()) * (d1.get_x() - d2.get_x()) + (d1.get_y() - d2.get_y()) * (d1.get_y() - d2.get_y()))/2            

        c2.add_updater(lambda mob: mob.move_to(md2))
        c2.add_updater(lambda mob: mob.become(Circle(distance(md2,md3)*1.1).move_to(md2).set_color(YELLOW)))
        c3.add_updater(lambda mob: mob.move_to(md3))
        c3.add_updater(lambda mob: mob.become(Circle(distance(md2,md3)*1.1).move_to(md3).set_color(YELLOW)))

        bisector.add_updater(lambda mob: mob.become(Line(ORIGIN,c0.point_at_angle(theta.get_value()/2)).set_color(PURE_GREEN)))

        line2.add_updater(lambda mob: mob.become(Line(ORIGIN,c0.point_at_angle(theta.get_value()))))

        self.play(theta.animate.set_value(250*DEGREES),run_time=6)
        self.play(theta.animate.set_value( 70*DEGREES),run_time=4)

        c2.clear_updaters()
        c3.clear_updaters()

        self.play(FadeOut(c2,c3),run_time=4)

        self.wait()

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))
def distance(d1, d2) -> float:
    return np.sqrt((d1[0] - d2[0]) * (d1[0] - d2[0]) + (d1[1] - d2[1]) * (d1[1] - d2[1]))           

class GetIntersections:

    def get_coord_from_proportion(self,vmob,proportion):
        return vmob.point_from_proportion(proportion)

    def get_points_from_curve(self, vmob, dx=0.005):
        coords = []
        for point in Range(0, 1, dx):
            dot = Dot(self.get_coord_from_proportion(vmob,point))
            coords.append(dot.get_center())
        return coords

    def get_intersections_between_two_vmobs(self, vmob1, vmob2,
                                            tolerance=0.05,
                                            radius_error=0.2,
                                            use_average=True,
                                            use_first_vmob_reference=False):
        coords_1 = self.get_points_from_curve(vmob1)
        coords_2 = self.get_points_from_curve(vmob2)
        intersections = []
        for coord_1 in coords_1:
            for coord_2 in coords_2:
                distance_between_points = distance(coord_1,coord_2)
                if use_average:
                    coord_3 = (coord_2 - coord_1) / 2
                    average_point = coord_1 + coord_3
                else:
                    if use_first_vmob_reference:
                        average_point = coord_1
                    else:
                        average_point = coord_2
                if len(intersections) > 0 and distance_between_points < tolerance:
                    last_intersection=intersections[-1]
                    distance_between_previus_point = distance(average_point,last_intersection)
                    if distance_between_previus_point > radius_error:
                        intersections.append(average_point)
                if len(intersections) == 0 and distance_between_points < tolerance:
                    intersections.append(average_point)
        return intersections


class copyAngle(Scene,GetIntersections):
    def construct(self):
        axes = NumberPlane().set_opacity(0.2)
        self.add(axes)

        t=Title("copy an angle over to a line of arbitrary direction ")
        self.play(Write(t))
        r=3

        default_rt=2

        p1=np.array([-5,-1,0])
        p0=np.array([-4,-3,0])
        p2=np.array([-2,-1,0])

        line1=Line(p0,p1)
        line2=Line(p0,p2)
        theta=Angle(line2,line1)
        thetaLabel=MathTex("\\theta").next_to(theta,UP)

        self.add(line1,line2,theta,thetaLabel)

        mp1=np.array([ 0, 1,0])
        mp2=np.array([ 5,-2,0])

        mline=Line(mp1,mp2)
        self.add(mline)

        mp3=np.array(mline.get_center()-0.5*mline.get_unit_vector())
        d3=Dot(mp3,radius=0.05,color=YELLOW)
        d0=d3.copy().move_to(p0)
        self.play(FadeIn(d0))

        c0=Circle(2,color=YELLOW).move_to(p0)
        self.play(GrowFromCenter(c0),run_time=default_rt)
        self.wait(default_rt)
        intersections = self.get_intersections_between_two_vmobs(c0, line1)
        for i in intersections:
            self.add(Dot(i,radius=0.05,color=PURE_GREEN))

        rp1=intersections[0]

        intersections = self.get_intersections_between_two_vmobs(c0, line2)
        for i in intersections:
            self.add(Dot(i,radius=0.05,color=PURE_BLUE))

        rp2=intersections[0]

        c0.generate_target()
        c0.target.move_to(d3)

        self.play(MoveToTarget(c0),ReplacementTransform(d0.copy(),d3),run_time=default_rt)

        intersections = self.get_intersections_between_two_vmobs(c0, mline)
#        for i in intersections:
#            self.(Dot(i,radius=0.05,color=PURE_GREEN))
        
        d4=Dot(intersections[0],radius=0.05,color=PURE_GREEN)
        self.play(FadeIn(d4))
#        self.play(FadeOut(c0))
        
        c1=Circle(distance(rp1,rp2)).move_to(rp1).set_color(PURE_GREEN)

        self.play(GrowFromCenter(c1),run_time=default_rt)
        self.wait(default_rt)
        rp1Dot=d4.copy().move_to(rp1)
        c1.generate_target()
        c1.target.move_to(d4)
        self.play(MoveToTarget(c1),ReplacementTransform(rp1Dot.copy(),d4),run_time=default_rt)

        intersections = self.get_intersections_between_two_vmobs(c0, c1)

        d5=Dot(intersections[0],radius=0.05,color=PURE_BLUE)
        self.play(FadeIn(d5))

        line35=Line(d3,d5)
        self.play(Write(line35),run_time=default_rt)
        newTheta=Angle(line35,Line(d3,mp1))
        newThetaLable=thetaLabel.copy().next_to(newTheta,UP)
        self.play(FadeIn(newTheta))
        self.play(ReplacementTransform(thetaLabel.copy(),newThetaLable),run_time=default_rt)
        self.play(FadeOut(c0),run_time=default_rt)
        self.play(FadeOut(c1),run_time=default_rt)

        self.wait(3)



class divideLine1(Scene):
    def construct(self):
        axes = NumberPlane().set_opacity(0.2)
        self.add(axes)

        t=Title("divide a line into 6 equal length segements")
        self.play(Write(t))
        num_points=7
        default_rt=2

        p0=np.array([-4,-1,0])
        p1=np.array([ 4, 1,0])
        d1=Dot(p1,radius=0.04,color=PURE_RED)
        line01=Line(p0,p1)
        self.add(line01)

        p2=np.array([ 5, 3,0])
        line02=Line(p0,p2).set_color(YELLOW)
        self.play(Write(line02),run_time=default_rt)
        unit=1.5
        c0=Circle(unit).set_color(PURE_RED).move_to(p0)

        unitVec02=line02.get_unit_vector()
        points = [p0 +  unit*n*unitVec02 for n in range(num_points)]
        colorList=[PURE_RED,ORANGE,YELLOW,PURE_GREEN,PURE_BLUE,LIGHT_PINK]
        d=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,color_gradient(colorList,len(points)))]

        mDot=d[0]
        c0.add_updater(lambda mob: mob.move_to(mDot.get_center()))
        self.play(FadeIn(c0))
        for dd in d[1:-1]:
            self.play(FadeIn(dd))
            self.play(
                Transform(
                    mDot,
                    dd,
#                    path_func=utils.paths.path_along_arc(TAU * 1 / 6),
#                    run_time=2,
                    rate_func=linear)
            )        
        self.play(FadeIn(d[-1]))
#        self.play(FadeOut(c0))
        lined1=Line(d[-1],p1).set_color(PURE_GREEN)
        self.play(Write(lined1))

        #draw a parallel line to line01 from p1 with same lenght
        r1=np.linalg.norm(d[-1].get_center()-p0)
        c1=Circle(r1,color=PURE_BLUE).move_to(d[-1])
        self.play(GrowFromCenter(c1),run_time=default_rt)
        self.play(c1.animate.move_to(p1),ReplacementTransform(d[-1].copy(),d1),run_time=default_rt)
        r2=np.linalg.norm(d[-1].get_center()-p1)
        c2=Circle(r2,color=PURE_GREEN).move_to(d[-1])
        self.play(GrowFromCenter(c2))
        c2.generate_target()
        c2.target.move_to(p0)
        self.play(MoveToTarget(c2),run_time=default_rt+1)

        p3=p0 + (p1 - d[-1].get_center())
        d3=Dot(p3,radius=0.04,color=PURE_RED)
        self.play(FadeIn(d3))
        line03=Line(p0,p3).set_color(PURE_GREEN)
        self.play(Write(line03))
        line13=Line(p3,p1).set_color(YELLOW)
        self.play(Write(line13))

        self.play(FadeOut(c1))
        self.play(FadeOut(c2))

        unitVec13=line13.get_unit_vector()
        points = [p1 -  unit*n*unitVec13 for n in range(num_points)]
        e=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,color_gradient(reversed(colorList),len(points)))]

        for dd in e[:-1]:
            self.play(FadeIn(dd))
            self.play(
                Transform(
                    mDot,
                    dd,
#                    run_time=2,
                    rate_func=linear)
            )
        self.play(FadeIn(e[-1]))
        self.play(FadeOut(c0))
        # draw 5 parallel line in parallel
        unitVec01=line01.get_unit_vector()
        unit=np.linalg.norm(p1-p0)/6
        points = [p0 + unit*n*unitVec01 for n in range(num_points)]
        b=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,color_gradient(colorList,len(points)))]

        pp=VGroup()
        actions=[]
        for i in range(len(d)):
            pp.add(Line(d[i],e[-1*i-1]).set_color(d[i].get_color()))
            actions.append(Write(pp[-1]))
        self.play(*actions)
        self.play(FadeIn(*b))

        self.play(FadeOut(line02,line13))
        self.play(FadeOut(pp,*d,*e,lined1,line03, d3))

        self.wait(10)


class DrawPolygonBase(ThreeDScene):
    default_rt=2
    def segmentUnitLength(self, line: Line, numberOfSegments: int, angleAwayFrom= 30*DEGREES, extend=1.3, extra=1.2) -> float:
        p0=line.get_start()
        lineLen=line.get_length()
        scaleLineLen=lineLen*extend*extra
        p2=p0+scaleLineLen*np.cos(angleAwayFrom)*UP+scaleLineLen*np.sin(angleAwayFrom)*LEFT
        line02=Line(p0,p2).set_color(YELLOW)
        self.play(Write(line02),run_time=self.default_rt)
        unit=lineLen*extend/numberOfSegments
        c0=Circle(unit).set_color(PURE_RED).move_to(p0)

        unitVec02=line02.get_unit_vector()
        num_points=numberOfSegments+1
        points = [p0 +  unit*n*unitVec02 for n in range(num_points)]
        colorList=[PURE_RED,ORANGE,YELLOW,PURE_GREEN,PURE_BLUE,LIGHT_PINK]
        d=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,color_gradient(colorList,len(points)))]

        mDot=d[0]
        c0.add_updater(lambda mob: mob.move_to(mDot.get_center()))
        self.play(FadeIn(c0))
        for dd in d[1:-1]:
            self.play(FadeIn(dd))
            self.play(
                Transform(
                    mDot,
                    dd,
#                    path_func=utils.paths.path_along_arc(TAU * 1 / 6),
#                    run_time=2,
                    rate_func=linear)
            )        
        self.play(FadeIn(d[-1]))
#        self.play(FadeOut(c0))
        p1=line.get_end()
        lined1=Line(d[-1],p1).set_color(PURE_GREEN)
        self.play(Write(lined1))

        #draw a parallel line to line01 from p1 with same lenght
        r1=np.linalg.norm(d[-1].get_center()-p0)
        c1=Circle(r1,color=PURE_BLUE).move_to(d[-1])
        self.play(GrowFromCenter(c1),run_time=self.default_rt)
        d1=Dot(p1,radius=0.04,color=PURE_RED)
        self.play(c1.animate.move_to(p1),ReplacementTransform(d[-1].copy(),d1),run_time=self.default_rt)
        r2=np.linalg.norm(d[-1].get_center()-p1)
        c2=Circle(r2,color=PURE_GREEN).move_to(d[-1])
        self.play(GrowFromCenter(c2))
        c2.generate_target()
        c2.target.move_to(p0)
        self.play(MoveToTarget(c2),run_time=self.default_rt+1)

        p3=p0 + (p1 - d[-1].get_center())
        d3=Dot(p3,radius=0.04,color=PURE_RED)
        self.play(FadeIn(d3))
        line03=Line(p0,p3).set_color(PURE_GREEN)
        self.play(Write(line03))
        line13=Line(p3,p1).set_color(YELLOW)
        self.play(Write(line13))

        self.play(FadeOut(c1))
        self.play(FadeOut(c2))

        unitVec13=line13.get_unit_vector()
        points = [p1 -  unit*n*unitVec13 for n in range(num_points)]
        e=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,color_gradient(reversed(colorList),len(points)))]

        for dd in e[:-1]:
            self.play(FadeIn(dd))
            self.play(
                Transform(
                    mDot,
                    dd,
#                    run_time=2,
                    rate_func=linear)
            )
        self.play(FadeIn(e[-1]))
        self.play(FadeOut(c0))
        # draw 5 parallel line in parallel
        unitVec01=line.get_unit_vector()
        unit=np.linalg.norm(p1-p0)/6
        points = [p0 + unit*n*unitVec01 for n in range(num_points)]
        b=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,color_gradient(colorList,len(points)))]

        pp=VGroup()
        actions=[]
        for i in range(len(d)):
            pp.add(Line(d[i],e[-1*i-1]).set_color(d[i].get_color()))
            actions.append(Write(pp[-1]))
        self.play(*actions)
        self.play(FadeIn(*b))

        self.play(FadeOut(line02,line13))
        self.play(FadeOut(pp,*d,*e,lined1,line03, d3))

        return unit
    
    def drawCircleAndPolygon(self, centre: np.ndarray, radius: float, numberOfPoints: int, fillColor = None, strokeColor = WHITE ):
        # baseRadius is the circumscribe circle radius 
        # of the base hexagon with same lenght as the required regular polygon side lenght
        baseRadius=radius*6/numberOfPoints         
        cDot=Dot(ORIGIN,radius=0.04)
        disposeGroup=VGroup().add(cDot)
        # circumscribing circle, rotate 90 degree clockwise to make the draw start from 6 o'clock direction
        c = Circle(radius).set_stroke(width=2).set_stroke(PURE_RED,opacity=0.75).rotate(-90*DEGREES).move_to(centre)
#            self.play(Write(c))
        angles = [(n * (360 / numberOfPoints) - 90) % 360 for n in range(numberOfPoints)]
        # Points on circumference of circle
        # First corner d[0] at 6 o'clock position 
        points = [c.point_at_angle(n*DEGREES) for n in angles]
        colourList = color_gradient([PURE_RED,ORANGE,YELLOW,PURE_GREEN,PURE_BLUE,LIGHT_PINK],len(points))
        d=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,colourList)]
        downDot=Dot(DOWN*baseRadius, color=WHITE,radius=0.04)
        disposeGroup.add(downDot)
        # draw circle
        baseR=Line(cDot,downDot).set_stroke(strokeColor)
        disposeGroup.add(baseR)
        r=baseR.copy().set_color(YELLOW)
        disposeGroup.add(r)
        ccDot=cDot.copy()
        disposeGroup.add(ccDot)
        r.add_updater(lambda mob: mob.put_start_and_end_on(ccDot.get_center(),downDot.get_center()))
        self.add(r)
        self.play(ccDot.animate.move_to(centre))
        self.play(Create(c),MoveAlongPath(downDot,c), run_time=self.default_rt,rate_func=rate_functions.ease_out_expo)
#        self.play(FadeIn(c))
        r.clear_updaters()
#            self.play(Write(r),FadeIn(downDot),run_time=default_rt)
        # drawing the first edge of the polygon by rotating the fix baseR (hexagon edge length)
        mDot=cDot.copy()
        disposeGroup.add(mDot)
        ## -baseRadius: -ve for the arc path be countwise
        arc= ArcBetweenPoints(start=mDot.get_center(), end=d[1].get_center(), stroke_color=YELLOW, radius=-baseRadius)
        self.play(FadeIn(baseR),run_time=self.default_rt)
        baseR.add_updater(lambda mob: mob.put_start_and_end_on(mDot.get_center(),downDot.get_center()))
        self.play(MoveAlongPath(mDot,arc),run_time=self.default_rt)
        baseR.clear_updaters()
        # flip the fix edge around the circumcribing circle
        disposeGroup.add()
        e: list[Line]=[]
        for i in ([*range(1,len(points))]):
            newDot=d[i-1]
            if i == numberOfPoints - 1: 
                arc= ArcBetweenPoints(start=d[i-1].get_center(), end=downDot.get_center(), stroke_color=YELLOW, radius=-baseRadius)
            else:
                arc= ArcBetweenPoints(start=d[i-1].get_center(), end=d[i+1].get_center(), stroke_color=YELLOW, radius=-baseRadius)
            e.append(Line(d[i],newDot).set_stroke(strokeColor))
            self.add(e[-1])
            e[-1].add_updater(lambda mob: mob.put_start_and_end_on(d[i].get_center(),newDot.get_center()))
            self.play(MoveAlongPath(newDot,arc))            
            e[-1].clear_updaters()
            disposeGroup.add(e[-1])
            self.add(e[-1])

        p=Polygon(*points).set_stroke(strokeColor)
        self.add(p)
        self.play(FadeOut(disposeGroup))
        self.play(FadeOut(*d))

        if fillColor!=None:
            self.play(p.animate.set_color(fillColor).set_opacity(1),run_time=self.default_rt)

        return c,p


class divideLine(DrawPolygonBase):
    def construct(self):
        axes = NumberPlane().set_opacity(0.2)
        self.add(axes)

        t=Title("divide a line into 6 equal length segements")
        self.play(Write(t))
        num_points=7
        default_rt=2

        p0=np.array([-4,-1,0])
        p1=np.array([ 4, 1,0])
        d1=Dot(p1,radius=0.04,color=PURE_RED)
        line01=Line(p0,p1)
        self.add(line01)

        unitLen=self.segmentUnitLength(line01,6, -65*DEGREES)

        self.wait(10)


class drawHeptagon(DrawPolygonBase):
    def construct(self):
#        axes = NumberPlane().set_opacity(0.2)
#        self.add(axes)

        default_rt=2

        p0=ORIGIN
        p1=np.array([ 0, -3,0])
        d1=Dot(p1,radius=0.04,color=PURE_RED)
        line01=Line(p1,p0)
        self.add(line01)

        unitLen=self.segmentUnitLength(line01,6)
        heptagonCenter=ORIGIN+UP*unitLen
        extendLine=Line(ORIGIN,heptagonCenter,color=PURE_GREEN)
        extendCircle=Circle(unitLen,color=PURE_GREEN)
        self.play(Write(extendLine),Write(extendCircle),run_time=default_rt)
        circle, heptagon = self.drawCircleAndPolygon(heptagonCenter,3+unitLen,7,fillColor=PURE_GREEN) 
        self.play(FadeOut(extendCircle,circle))

        self.wait(10)

class drawOctagon(Scene):
    def construct(self):
        default_rt=2
        self.play(Write(Title("Draw Regular Octagon with straight ruler and compass").scale(0.8)))
        c = Circle(2).set_stroke(width=2).set_stroke(PURE_RED,opacity=0.5)
        sideLen=2*np.sin(22.5*DEGREES)*2
        self.play(Write(c))

        num_points = 8
        # Calculate each angle
        angles = [(n * (360 / num_points) +90) % 360 for n in range(num_points)]
        # Points on circumference of circle
        # First point at the top
        points = [c.point_at_angle(n*DEGREES) for n in angles]
        colourList = color_gradient([PURE_RED,ORANGE,YELLOW,PURE_GREEN,PURE_BLUE,LIGHT_PINK],len(points))

        d=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,colourList)]

        origin=Dot(radius=0.04)
        self.add(origin)

#        traceDot=TracedPath(centre.get_center)
#        self.add(traceDot)

        leftDot=Dot(LEFT*2, color=PURE_GREEN,radius=0.04)
        rightDot=Dot(RIGHT*2, color=PURE_GREEN,radius=0.04)
        self.add(leftDot)
        lineH=Line(leftDot,rightDot)
        self.play(Write(lineH))
        self.add(rightDot)
        leftCircle=Circle(2.1).set_stroke(width=2).set_color(PURE_GREEN).move_to(LEFT*2)
        rightCircle=Circle(2.1).set_stroke(width=2).set_color(PURE_GREEN).move_to(RIGHT*2)
        # vertic bisector
        self.play(GrowFromPoint(leftCircle,leftDot),GrowFromPoint(rightCircle,rightDot))
        lineB1=Line(UP*2.5,DOWN*2.5)
        self.play(Write(lineB1))
        # diagonal bisector
        rightCircle.add_updater(lambda mob: mob.move_to(rightDot.get_center()))
        quarter=ArcBetweenPoints(start=points[6], end=points[0], stroke_color=YELLOW, radius=2)
        self.play(MoveAlongPath(rightDot,quarter),run_time=default_rt)
        line45=Line(c.get_corner(UL)*1.2,c.get_corner(DR)*1.2)
        self.play(Write(line45))
        self.play(FadeOut(leftCircle,rightCircle))
        rightCircle.clear_updaters()

        line0=Line(d[0],d[1])
        self.play(Write(line0))
        e: list[Line] = []
        disposeGroup=VGroup(line0)
        dummy=d[0].copy()
        for i in ([*range(1,len(points))]):
            newDot=d[i-1]
            if i == num_points - 1: 
                arc= ArcBetweenPoints(start=d[i-1].get_center(), end=dummy.get_center(), stroke_color=YELLOW, radius=-sideLen)
            else:
                arc= ArcBetweenPoints(start=d[i-1].get_center(), end=d[i+1].get_center(), stroke_color=YELLOW, radius=-sideLen)
            e.append(Line(d[i],newDot))
            self.add(e[-1])
            e[-1].add_updater(lambda mob: mob.put_start_and_end_on(d[i].get_center(),newDot.get_center()))
            self.play(MoveAlongPath(newDot,arc))            
            e[-1].clear_updaters()
            disposeGroup.add(e[-1])
            self.add(e[-1])

        p=Polygon(*points).set_color(YELLOW)
        self.play(Unwrite(lineB1),Unwrite(lineH),Unwrite(line45))
        self.play(FadeOut(disposeGroup,c,*d,leftDot,rightDot,origin,newDot),p.animate.set_opacity(0.8),run_time=default_rt)

        self.wait(3)

class drawOctagonAndCubes(DrawPolygonBase):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.play(distance_to_origin.animate.set_value(0.62))
        octagonCenter=UP
        circle, octagon = self.drawCircleAndPolygon(octagonCenter,4,8) 
        self.play(FadeOut(circle))   
        self.play(octagon.animate.move_to(ORIGIN).rotate(22.5*DEGREES))
        sideLen=3
        
        squares=[*list(map(lambda d: Square(sideLen).align_to(octagon,direction=d),[LEFT,UP,RIGHT,DOWN]))]

        m=Square(3)
        self.play(GrowFromCenter(m))
        self.play(Transform(m,squares[0]))

        self.add(squares[0])
        for s in squares[1:]+[squares[0]]:
            startPoints=[*list(map(lambda d: m.get_corner(d), [UL,UR,DR,DL]))]
            endPoints  =[*list(map(lambda d: s.get_corner(d), [UL,UR,DR,DL]))]
            lines = [*list(map(lambda start,end: Line(start,end),startPoints,endPoints))]
            actions = [*list(map(lambda line: Write(line),lines))]
            self.play(*actions,Transform(m,s),run_time=self.default_rt)
            self.add(s)
        self.wait(5)

class repeating(ThreeDScene):
    def construct(self):
        default_rt=2
        numberOfPoints=8
        circle=Circle(4)
        angles = [(n * (360 / numberOfPoints) +22.5) % 360 for n in range(numberOfPoints)]
        points = [circle.point_at_angle(n*DEGREES) for n in angles]

        octagon=Polygon(*points)
        self.play(GrowFromCenter(octagon))

        sideLen=3
        
        squares=[*list(map(lambda d: Square(sideLen).align_to(octagon,direction=d),[LEFT,UP,RIGHT,DOWN]))]

        m=Square(3)
        self.play(GrowFromCenter(m))
        self.play(Transform(m,squares[0]))

        repeatingUnit=VGroup(*squares)

        self.add(squares[0])
        for s in squares[1:]+[squares[0]]:
            startPoints=[*list(map(lambda d: m.get_corner(d), [UL,UR,DR,DL]))]
            endPoints  =[*list(map(lambda d: s.get_corner(d), [UL,UR,DR,DL]))]
            lines = [*list(map(lambda start,end: Line(start,end),startPoints,endPoints))]
            repeatingUnit.add(*lines)
            actions = [*list(map(lambda line: Write(line),lines))]
            self.play(*actions,Transform(m,s),run_time=default_rt)
            self.add(s)

        actions = [*list(map(lambda s,d: s.copy().animate.next_to(s,d,buff=0.0),squares,[LEFT,UP,RIGHT,DOWN]))]
        self.play(*actions,run_time=default_rt)

        actions = [*list(map(lambda d: repeatingUnit.copy().animate.move_to(d*4*np.cos(np.pi/8)*np.sqrt(2)),[UL,UR,DR,DL]))]


        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.play(distance_to_origin.animate.set_value(0.42),*actions,run_time=default_rt)

        actions = [*list(map(lambda d: repeatingUnit.copy().animate.move_to(d*(4*np.cos(np.pi/8)*2+3)),[LEFT,UP,RIGHT,DOWN]))]
        self.play(*actions,run_time=default_rt)

        self.wait(5)

class drawNonagon(DrawPolygonBase):
    def construct(self):
#        self.play(Write(MathTex("Draw\ Regular\ Nonagon\ by\ scale\ up\ the\ circumscribe\ circle\ of\ the\ base\ hexagon\ by\ 1.5\ times").scale(0.3).to_edge(BOTTOM)))
#        axes = NumberPlane(x_range=[-10,10,1]).set_opacity(0.2)
#        self.add(axes)
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.play(distance_to_origin.animate.set_value(0.62))

        default_rt=2
        baseRadius=3
        cDot=Dot(radius=0.04)
        self.add(cDot)

        cc = Circle(3).set_stroke(width=2).set_stroke(PURE_RED,opacity=0.75).rotate(-90*DEGREES)
        self.play(Write(cc))
        downDot=Dot(DOWN*baseRadius, color=WHITE,radius=0.04)

        # Equaliteral Triangle
        angles = [(n * (360 / 6) - 90) % 360 for n in range(6)]
        points = [cc.point_at_angle(n*DEGREES) for n in angles]
        colourList = color_gradient([PURE_RED,ORANGE,YELLOW,PURE_GREEN,PURE_BLUE,LIGHT_PINK],len(points))
        dd=[*map(lambda p,c: Dot(p,radius=0.04,color=c),points,colourList)]
        # bisector
        downCircle =cc.copy().set_color(PURE_GREEN).move_to(DOWN*3)
        leftCircle =cc.copy().set_color(PURE_BLUE ).move_to(dd[1])
        rightCircle=cc.copy().set_color(YELLOW    ).move_to(dd[-1])
        circles=VGroup(downCircle,leftCircle,rightCircle)
        self.play(ReplacementTransform(cc.copy(),downCircle))
        self.play(FadeIn(dd[-1],dd[1]))
        self.play(ReplacementTransform(downCircle.copy(),leftCircle),ReplacementTransform(downCircle.copy(),rightCircle), run_time=default_rt)
        r=Line(cDot,downDot)
        self.play(Write(r),FadeIn(downDot),run_time=default_rt)

        triangle=VGroup(Line(dd[0],dd[2]),Line(dd[2],dd[4]),Line(dd[4],dd[0]))
        for line in triangle.submobjects:
            self.play(Write(line))
        self.play(circles.animate.set_stroke(opacity=0.3),run_time=default_rt)
        self.play(triangle.animate.set_opacity(0.3),run_time=default_rt)

        circle6, hexagon = self.drawCircleAndPolygon(ORIGIN, baseRadius, 6)
        self.play(FadeOut(circles,circle6,cc,dd[-1],dd[1]),run_time=default_rt)
        circle9, nonagon = self.drawCircleAndPolygon(UP*1.5, 4.5, 9, fillColor=YELLOW)
        self.play(FadeOut(triangle,circle9),run_time=default_rt)

        self.wait(2)

class endGame(DrawPolygonBase):
    def construct(self):    
        def camera_moveto(self, c: np.array):
            self.camera.frame_center=c
        default_rt=2
        axes = NumberPlane(x_range=[-20,20,0.5],y_range=[-12,12,0.5]).set_opacity(0.2)
        self.add(axes)
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        d=distance_to_origin.get_value()
        centerY=ValueTracker(0)
        self.camera.frame_center=np.array([0.0,centerY.get_value(),0.0])
        self.add_updater(lambda Y: camera_moveto(self,np.array([0.0,centerY.get_value(),0.0]))) 
        circles=VGroup()

        start=6
        end=13
        colourList = color_gradient([PURE_RED,ORANGE,YELLOW,PURE_GREEN,PURE_BLUE,PURPLE],end-start)
        for i in range(start,end):
            c,p = self.drawCircleAndPolygon(ORIGIN+UP*(i*0.5-3),i/2,i,strokeColor=colourList[i-start])
            circles.add(c)
            self.play(distance_to_origin.animate.set_value(d*(1-i/12*0.4)),centerY.animate.set_value((i-5)*0.5),run_time=default_rt)
        for c in reversed(circles.submobjects):
            self.play(FadeOut(c))    
        self.wait(10)
