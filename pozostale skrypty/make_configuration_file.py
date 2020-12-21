import os
import glob
import re

con=open('config.txt','r').readlines()
PATH_TO_TEST_IMAGES_DIR_m = './'
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.yuv')
list_of_images_m = glob.glob(searchstr_m)
t0=con[0].replace('\n','')
t1=con[1]
z=0
r=0
num_file=1
licz=0
l_fot=3 # ile w configu pojedynczym zdjec
a=len(list_of_images_m)
if(a%2==0):
    while(licz<len(list_of_images_m)):
        if os.path.exists("./DERS7_Kermit_07"+str(num_file)+".cfg"):
            os.remove("./DERS7_Kermit_07"+str(num_file)+".cfg")
        kernit2=open("./DERS7_Kermit_07"+str(num_file)+".cfg", "a+")
        kernit2.write('#=============== GENERAL PARAMETERS =================\n')
        kernit2.write('SourceWidth           '+str(t0)+'\n')
        kernit2.write('SourceHeight          '+str(t1)+'\n')
        kernit2.write('\n')
        kernit2.write('StartFrame            0'+'\n')
        kernit2.write('TotalNumberOfFrames   1'+'\n')
        kernit2.write('\n')
        kernit2.write('FileCameraParameter   cam_param_dog.txt'+'\n')
        kernit2.write('\n')
        kernit2.write('DepthType             0     # 0...from camera, 1...from world origin'+'\n')
        kernit2.write('#DepthFormat           400   # 400...YUV400, 420...YUC420'+'\n')
        kernit2.write('\n')
        kernit2.write('#=============== CAMERA CONFIGURATION ================'+'\n')    
        kernit2.write('\n')
        kernit2.write('NumberOfInputViews    '+str(3)+'\n')
        kernit2.write('NumberOfOutputDepths   '+str(3)+'\n')
        kernit2.write('\n')
        z=licz
        for l in range(l_fot):
            kernit2.write('InputCameraName'+str(l)+'      param_v0'+str(z)+'\n')
            z+=1
        kernit2.write('\n')
        z=licz
        for l in range(l_fot):
            kernit2.write('OutputCameraName'+str(l)+'      param_v0'+str(z)+'\n')
            z+=1
        kernit2.write('\n')
        kernit2.write('#=============== INPUT PARAMETERS ================\n')
        kernit2.write('\n')
        z=licz
        for l in range(l_fot):
            kernit2.write("FileInputViewImage"+str(l)+"      "+"zdj"+str(0)+str(z)+"_"+str(t0)+"x"+str(t1)+".yuv"+'\n')
            z+=1
        kernit2.write('\n')
        kernit2.write('#=============== OUTPUT PARAMETERS ================\n')
        z=licz
        for l in range(l_fot):
            kernit2.write("FileOutputDepthMapImage"+str(l)+" E_"+str(0)+str(z)+"_"+str(t0)+"x"+str(t1)+"_0_3_1_62d_16bps_cf400.yuv"+"\n")
            z+=1
        kernit2.write('\n')
        kernit2.write('#=============== DEGUB PARAMETERS ==================\n')
        kernit2.write('\n')
        kernit2.write('OutputErrors            0  # Store matching cost to files 0..Off 1..On\n')
        kernit2.write('\n')
        z=licz
        for l in range(l_fot):
            kernit2.write("FileOutputErrors"+str(1)+"_"+str(l)+"     Errors_20_"+str(0)+str(z)+"_"+str(t0)+"x"+str(t1)+"_8bps_cf400.yuv"+"\n")
            z+=1
        z=licz
        r=licz
        kernit2.write('\n')
        kernit2.write('#=============== OLD PARAMETERS ==================\n')
        kernit2.write('\n')
        kernit2.write('LeftCameraName        param_v0'+str(z)+'\n')
        kernit2.write('CenterCameraName      param_v0'+str(z+1)+'\n')
        kernit2.write('RightCameraName       param_v0'+str(z+2)+'\n')
        kernit2.write('FileLeftViewImage       zdj0'+str(r)+'_'+str(t0)+'x'+str(t1)+'.yuv'+'\n')
        kernit2.write('FileCenterViewImage       zdj0'+str(r+1)+'_'+str(t0)+'x'+str(t1)+'.yuv'+'\n')
        kernit2.write('FileRightViewImage       zdj0'+str(r+2)+'_'+str(t0)+'x'+str(t1)+'.yuv'+'\n')
        kernit2.write('FileOutputDepthMapImage 	v3_1000x750_0_3_1_62d_16bps_cf400.yuv\n')
        kernit2.write('\n')
        kernit2.write('#=============== SEARCH PARAMETERS ================\n')
        kernit2.write('\n')
        kernit2.write('SearchRangeType                         1   # 0...Min/MaxDisparity, 1...Znear/Zfar\n')
        kernit2.write('\n')
        kernit2.write('#------------ For SearchRangeType = 0 -------------\n')
        kernit2.write('MinimumValueOfDisparitySearchRange      -10\n')
        kernit2.write('MaximumValueOfDisparitySearchRange      50 \n')
        kernit2.write('MinimumValueOfDisparityRange            -10\n')
        kernit2.write('MaximumValueOfDisparityRange            50\n')
        kernit2.write('SearchLevel                             1   # 1...integer, 2...half, 4...quarter, 8...1/8 pixel\n')
        kernit2.write('BaselineBasis                           0   # cam distance from 0...min of left or right, 1...max of left or right, 2...left, 3...right, 4...top, 5...bottom\n')
        kernit2.write('\n')
        kernit2.write('#------------ For SearchRangeType = 1 -------------\n')
        kernit2.write('NearestDepthValue                       1.62\n')
        kernit2.write('FarthestDepthValue                      4.55\n')
        kernit2.write('NearestSearchDepthValue                 1.62	#0.31\n')
        kernit2.write('FarthestSearchDepthValue                4.55\n')
        kernit2.write('NumberOfDepthSteps                      200\n')
        kernit2.write('\n')
        kernit2.write('#============== MATCHING PARAMETERS ================\n')
        kernit2.write('\n')
        kernit2.write('MatchingMethod                          2 #2   # 0...???, 1...disparity-based block, 2...homography-based block, 3...disparity-based soft-segmentation-base\n')
        kernit2.write('MatchingBlock                           3    # 1...pixel matching, 3...3x3 block matching\n')
        kernit2.write('\n')
        kernit2.write('#DisparityDirection                     0    # 0...Conventinal, 1...Horizontal, 2...Vertical # na poczatku byl #\n')
        kernit2.write('Precision                               2   # horizontal precision: 1...integer, 2...half, 4...quarter, 8...1/8 pixel\n')
        kernit2.write('VerticalPrecision                       2    # vertical   precision: 1...integer, 2...half, 4...quarter, 8...1/8 pixel\n')
        kernit2.write('Filter                                  0    # upsample horizontal filter: 0...bi-linear, 1...bi-cubic supports 1/8pixel and 2...MPEG-4 AVC 6-tap support upto 1/4pixel.\n')
        kernit2.write('VerticalFilter                          0    # upsample vertical   filter: 0...bi-linear, 1...bi-cubic supports 1/8pixel and 2...MPEG-4 AVC 6-tap support upto 1/4pixel.\n')
        kernit2.write('\n')
        kernit2.write('#------------ For MatchingMethod = 3 -------------\n')
        kernit2.write('SoftBlockWidth          5\n')
        kernit2.write('SoftBlockHeight         5\n')
        kernit2.write('SoftColorCoeff          20.0\n')
        kernit2.write('SoftDistanceCoeff       20.0\n')
        kernit2.write('\n')
        kernit2.write('#========== Occlusion ========== \n')
        kernit2.write('\n')
        kernit2.write('Occlusion               0\n')
        kernit2.write('\n')
        kernit2.write('#========== Segmentation ==========\n')
        kernit2.write('\n')
        kernit2.write('ImageSegmentation       0   # 0...off, 1...on difficult to use\n')
        kernit2.write('SegmentationMethod      1   # 1...mean shift, 2...phyramidal, 3...kernel clustering\n')
        kernit2.write('MaxCluster              10  # positive integer value\n')
        kernit2.write('\n')
        kernit2.write('#========== Semi-automatic Depth Estimation ==========\n')
        kernit2.write('\n')
        kernit2.write('DepthEstimationMode     0   # 0...automatic (Graph-Cuts) 1...semi-automatic 1, 2...semi-automatic 2, 3...reference depth mode\n')
        kernit2.write('\n')
        kernit2.write('SmoothingCoefficient                    2.0 		# SC1 for non-edge\n')
        kernit2.write('SmoothingCoefficient2                    2.0			# SC2, SC1*SC2 for edge\n')
        kernit2.write('\n')
        kernit2.write('#---- For DepthEstimationMode = 1 or 2  ------\n')
        kernit2.write('FileCenterManual                #Path and filename prefix of the manual input files\n')
        kernit2.write('\n')
        kernit2.write('#---- For DepthEstimationMode = 2  ------\n')
        kernit2.write('ThresholdOfDepthDifference      # Threshold value of depth difference\n')
        kernit2.write('MovingObjectsBSize              # 0: small  1: medium  2: large\n')
        kernit2.write('MotionSearchBSize               # 0: narrow 1: medium 2: wide\n')
        kernit2.write('\n')
        kernit2.write('#---- For DepthEstimationMode = 3  ------\n')
        kernit2.write('\n')
        kernit2.write('RefDepthCameraName              # camera parameter name\n')
        kernit2.write('RefDepthFile                   	# filename reference depthmap video\n')
        kernit2.write('\n')
        kernit2.write('#---- For DepthEstimationMode = 4  ------\n')
        kernit2.write('ReliabilityThreshold	0		# rTh. if texture slope S < rTh, matching error is weighted by *rTh/S\n')
        kernit2.write('SmoothingThreshold		12		# sTh. if texture slope S < sTh, depth smoothing coefficient SC1 is weighted by *SC2*sTh/S\n')
        kernit2.write('\n')
        kernit2.write('#========== Temporal Enhancement ==========\n')
        kernit2.write('TemporalEnhancement     0 		# acceleration: 0...off, 1...on skips no-motion pixel in frame\n')
        kernit2.write('Threshold               1.00 	# motion detection, pixel difference in two frames\n')
        kernit2.close()
        licz+=3
        num_file+=1
else:
    while(licz<len(list_of_images_m)):
        if os.path.exists("./DERS7_Kermit_07"+str(num_file)+".cfg"):
            os.remove("./DERS7_Kermit_07"+str(num_file)+".cfg")
        kernit2=open("./DERS7_Kermit_07"+str(num_file)+".cfg", "a+")
        kernit2.write('#=============== GENERAL PARAMETERS =================\n')
        kernit2.write('SourceWidth           '+str(t0)+'\n')
        kernit2.write('SourceHeight          '+str(t1)+'\n')
        kernit2.write('\n')
        kernit2.write('StartFrame            0'+'\n')
        kernit2.write('TotalNumberOfFrames   1'+'\n')
        kernit2.write('\n')
        kernit2.write('FileCameraParameter   cam_param_dog.txt'+'\n')
        kernit2.write('\n')
        kernit2.write('DepthType             0     # 0...from camera, 1...from world origin'+'\n')
        kernit2.write('#DepthFormat           400   # 400...YUV400, 420...YUC420'+'\n')
        kernit2.write('\n')
        kernit2.write('#=============== CAMERA CONFIGURATION ================'+'\n')    
        kernit2.write('\n')
        kernit2.write('NumberOfInputViews    '+str(3)+'\n')
        kernit2.write('NumberOfOutputDepths   '+str(3)+'\n')
        kernit2.write('\n')
        z=licz
        if z!=0 and z%(a-1)==0:
            z=licz-1
        for l in range(l_fot):
            kernit2.write('InputCameraName'+str(l)+'      param_v0'+str(z)+'\n')
            z+=1
        kernit2.write('\n')
        z=licz
        if z!=0 and z%(a-1)==0:
            z=licz-1
        for l in range(l_fot):
            kernit2.write('OutputCameraName'+str(l)+'      param_v0'+str(z)+'\n')
            z+=1
        kernit2.write('\n')
        kernit2.write('#=============== INPUT PARAMETERS ================\n')
        kernit2.write('\n')
        z=licz
        if z!=0 and z%(a-1)==0:
            z=licz-1
        for l in range(l_fot):
            kernit2.write("FileInputViewImage"+str(l)+"      "+"zdj"+str(0)+str(z)+"_"+str(t0)+"x"+str(t1)+".yuv"+'\n')
            z+=1
        kernit2.write('\n')
        kernit2.write('#=============== OUTPUT PARAMETERS ================\n')
        z=licz
        if z!=0 and z%(a-1)==0:
            z=licz-1
        for l in range(l_fot):
            kernit2.write("FileOutputDepthMapImage"+str(l)+" E_"+str(0)+str(z)+"_"+str(t0)+"x"+str(t1)+"_0_3_1_62d_16bps_cf400.yuv"+"\n")
            z+=1
        kernit2.write('\n')
        kernit2.write('#=============== DEGUB PARAMETERS ==================\n')
        kernit2.write('\n')
        kernit2.write('OutputErrors            0  # Store matching cost to files 0..Off 1..On\n')
        kernit2.write('\n')
        z=licz
        if z!=0 and z%(a-1)==0:
            z=licz-1
        for l in range(l_fot):
            kernit2.write("FileOutputErrors"+str(1)+"_"+str(l)+"     Errors_20_"+str(0)+str(z)+"_"+str(t0)+"x"+str(t1)+"_8bps_cf400.yuv"+"\n")
            z+=1
        z=licz
        if z!=0 and z%(a-1)==0:
            z=licz-1
        r=licz
        if r!=0 and r%(a-1)==0:
            r=licz-1
        kernit2.write('\n')
        kernit2.write('#=============== OLD PARAMETERS ==================\n')
        kernit2.write('\n')
        kernit2.write('LeftCameraName        param_v0'+str(z)+'\n')
        kernit2.write('CenterCameraName      param_v0'+str(z+1)+'\n')
        kernit2.write('RightCameraName       param_v0'+str(z+2)+'\n')
        kernit2.write('FileLeftViewImage       zdj0'+str(r)+'_'+str(t0)+'x'+str(t1)+'.yuv'+'\n')
        kernit2.write('FileCenterViewImage       zdj0'+str(r+1)+'_'+str(t0)+'x'+str(t1)+'.yuv'+'\n')
        kernit2.write('FileRightViewImage       zdj0'+str(r+2)+'_'+str(t0)+'x'+str(t1)+'.yuv'+'\n')
        kernit2.write('FileOutputDepthMapImage 	v3_1000x750_0_3_1_62d_16bps_cf400.yuv\n')
        kernit2.write('\n')
        kernit2.write('#=============== SEARCH PARAMETERS ================\n')
        kernit2.write('\n')
        kernit2.write('SearchRangeType                         1   # 0...Min/MaxDisparity, 1...Znear/Zfar\n')
        kernit2.write('\n')
        kernit2.write('#------------ For SearchRangeType = 0 -------------\n')
        kernit2.write('MinimumValueOfDisparitySearchRange      -10\n')
        kernit2.write('MaximumValueOfDisparitySearchRange      50 \n')
        kernit2.write('MinimumValueOfDisparityRange            -10\n')
        kernit2.write('MaximumValueOfDisparityRange            50\n')
        kernit2.write('SearchLevel                             1   # 1...integer, 2...half, 4...quarter, 8...1/8 pixel\n')
        kernit2.write('BaselineBasis                           0   # cam distance from 0...min of left or right, 1...max of left or right, 2...left, 3...right, 4...top, 5...bottom\n')
        kernit2.write('\n')
        kernit2.write('#------------ For SearchRangeType = 1 -------------\n')
        kernit2.write('NearestDepthValue                       1.52\n')
        kernit2.write('FarthestDepthValue                      11.55\n')
        kernit2.write('NearestSearchDepthValue                 1.52	#0.31\n')
        kernit2.write('FarthestSearchDepthValue                11.55\n')
        kernit2.write('NumberOfDepthSteps                      400\n')
        kernit2.write('\n')
        kernit2.write('#============== MATCHING PARAMETERS ================\n')
        kernit2.write('\n')
        kernit2.write('MatchingMethod                          2 #2   # 0...???, 1...disparity-based block, 2...homography-based block, 3...disparity-based soft-segmentation-base\n')
        kernit2.write('MatchingBlock                           3    # 1...pixel matching, 3...3x3 block matching\n')
        kernit2.write('\n')
        kernit2.write('#DisparityDirection                     0    # 0...Conventinal, 1...Horizontal, 2...Vertical # na poczatku byl #\n')
        kernit2.write('Precision                               2   # horizontal precision: 1...integer, 2...half, 4...quarter, 8...1/8 pixel\n')
        kernit2.write('VerticalPrecision                       2    # vertical   precision: 1...integer, 2...half, 4...quarter, 8...1/8 pixel\n')
        kernit2.write('Filter                                  0    # upsample horizontal filter: 0...bi-linear, 1...bi-cubic supports 1/8pixel and 2...MPEG-4 AVC 6-tap support upto 1/4pixel.\n')
        kernit2.write('VerticalFilter                          0    # upsample vertical   filter: 0...bi-linear, 1...bi-cubic supports 1/8pixel and 2...MPEG-4 AVC 6-tap support upto 1/4pixel.\n')
        kernit2.write('\n')
        kernit2.write('#------------ For MatchingMethod = 3 -------------\n')
        kernit2.write('SoftBlockWidth          5\n')
        kernit2.write('SoftBlockHeight         5\n')
        kernit2.write('SoftColorCoeff          20.0\n')
        kernit2.write('SoftDistanceCoeff       20.0\n')
        kernit2.write('\n')
        kernit2.write('#========== Occlusion ========== \n')
        kernit2.write('\n')
        kernit2.write('Occlusion               0\n')
        kernit2.write('\n')
        kernit2.write('#========== Segmentation ==========\n')
        kernit2.write('\n')
        kernit2.write('ImageSegmentation       0   # 0...off, 1...on difficult to use\n')
        kernit2.write('SegmentationMethod      1   # 1...mean shift, 2...phyramidal, 3...kernel clustering\n')
        kernit2.write('MaxCluster              10  # positive integer value\n')
        kernit2.write('\n')
        kernit2.write('#========== Semi-automatic Depth Estimation ==========\n')
        kernit2.write('\n')
        kernit2.write('DepthEstimationMode     0   # 0...automatic (Graph-Cuts) 1...semi-automatic 1, 2...semi-automatic 2, 3...reference depth mode\n')
        kernit2.write('\n')
        kernit2.write('SmoothingCoefficient                    4.0 		# SC1 for non-edge\n')
        kernit2.write('SmoothingCoefficient2                    4.0			# SC2, SC1*SC2 for edge\n')
        kernit2.write('\n')
        kernit2.write('#---- For DepthEstimationMode = 1 or 2  ------\n')
        kernit2.write('FileCenterManual                #Path and filename prefix of the manual input files\n')
        kernit2.write('\n')
        kernit2.write('#---- For DepthEstimationMode = 2  ------\n')
        kernit2.write('ThresholdOfDepthDifference      # Threshold value of depth difference\n')
        kernit2.write('MovingObjectsBSize              # 0: small  1: medium  2: large\n')
        kernit2.write('MotionSearchBSize               # 0: narrow 1: medium 2: wide\n')
        kernit2.write('\n')
        kernit2.write('#---- For DepthEstimationMode = 3  ------\n')
        kernit2.write('\n')
        kernit2.write('RefDepthCameraName              # camera parameter name\n')
        kernit2.write('RefDepthFile                   	# filename reference depthmap video\n')
        kernit2.write('\n')
        kernit2.write('#---- For DepthEstimationMode = 4  ------\n')
        kernit2.write('ReliabilityThreshold	0		# rTh. if texture slope S < rTh, matching error is weighted by *rTh/S\n')
        kernit2.write('SmoothingThreshold		12		# sTh. if texture slope S < sTh, depth smoothing coefficient SC1 is weighted by *SC2*sTh/S\n')
        kernit2.write('\n')
        kernit2.write('#========== Temporal Enhancement ==========\n')
        kernit2.write('TemporalEnhancement     0 		# acceleration: 0...off, 1...on skips no-motion pixel in frame\n')
        kernit2.write('Threshold               1.00 	# motion detection, pixel difference in two frames\n')
        kernit2.close()
        licz+=3
        num_file+=1
    