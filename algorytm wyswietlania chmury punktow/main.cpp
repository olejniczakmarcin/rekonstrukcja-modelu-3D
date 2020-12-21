#include <pcl/io/pcd_io.h>
#include <pcl/io/ply_io.h>
#include <pcl/io/vtk_io.h>
#include <pcl/io/io.h>
#include <pcl/io/vtk_lib_io.h>
#include <pcl/io/file_io.h>
#include <pcl/io/ply/ply_parser.h>
#include <pcl/io/ply/ply.h>
#include <pcl/point_types.h>
#include <pcl/visualization/pcl_visualizer.h>
#include <pcl/console/print.h>
#include <pcl/console/parse.h>
#include <pcl/console/time.h>
#include <pcl/range_image/range_image.h>
#include <pcl/common/transforms.h>
#include <pcl/common/geometry.h>
#include <pcl/common/common.h>
#include <pcl/common/common_headers.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/features/normal_3d.h>
#include <pcl/features/gasd.h>
#include <pcl/features/normal_3d_omp.h>
#include <pcl/filters/crop_box.h>
#include <pcl/filters/crop_hull.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/filters/passthrough.h>
#include <pcl/filters/extract_indices.h>
#include <pcl/filters/project_inliers.h>
#include <pcl/filters/radius_outlier_removal.h>
#include <pcl/filters/statistical_outlier_removal.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <pcl/segmentation/extract_clusters.h>
#include <pcl/surface/poisson.h>
#include <pcl/surface/mls.h>
#include <pcl/surface/simplification_remove_unused_vertices.h>
#include <pcl/surface/vtk_smoothing/vtk_utils.h>
#include <pcl/surface/gp3.h>
#include <pcl/surface/convex_hull.h>
#include <pcl/sample_consensus/method_types.h>
#include <pcl/sample_consensus/model_types.h>
#include <pcl/search/search.h>
#include <pcl/search/kdtree.h>
#include <boost/filesystem.hpp>
#include <boost/algorithm/algorithm.hpp>
#include <boost/thread/thread.hpp>
#include <iostream>
#include <fstream>
#include <string>

void vizualizeMesh2(pcl::PointCloud<pcl::PointXYZRGB>::Ptr & cloud) {

	boost::shared_ptr<pcl::visualization::PCLVisualizer> viewer(new pcl::visualization::PCLVisualizer("chmura"));
	int PORT1 = 0;
	viewer->createViewPort(0.0, 0.0, 1.0, 1.0, PORT1);
	viewer->setBackgroundColor(0, 0, 0, PORT1);
	viewer->addText("chmura", 10, 10, "PORT1", PORT1);

	viewer->addCoordinateSystem();
	pcl::PointXYZ p1, p2, p3;

	p1.getArray3fMap() << 0, 0, 1;
	p2.getArray3fMap() << 0, 1, 0;
	p3.getArray3fMap() << 1, 0.1, 0;

	viewer->addText3D("x", p1, 0.2, 1, 0, 0, "x_");
	viewer->addText3D("y", p2, 0.2, 0, 1, 0, "y_");
	viewer->addText3D("z", p3, 0.2, 0, 0, 1, "z_");

	if (cloud->points[0].r <= 0 && cloud->points[0].g <= 0 && cloud->points[0].b <= 0) {
		pcl::visualization::PointCloudColorHandlerCustom<pcl::PointXYZRGB> color_handler(cloud, 255, 255, 0);
		viewer->removeAllPointClouds(0);
		viewer->addPointCloud(cloud, color_handler, "original_cloud", PORT1);
	}
	else {
		viewer->addPointCloud(cloud, "original_cloud", PORT1);
	}

	viewer->initCameraParameters();
	viewer->resetCamera();

	std::cout << "Press [q] to exit!" << std::endl;
	while (!viewer->wasStopped()) {
		viewer->spin();
	}
}

int main(int argc, char **argv){

  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZRGB>());
  std::string name = (argc > 1) ? argv[1] : "newcloud.xyz";
  std::ifstream file(name);
  if (!file.is_open()) {
	  std::cout << "Error: Could not find " << argv[1] << std::endl;
	  return -1;
  }
  double x_, y_, z_,_r,_g,_b;
  while (file >> x_ >> y_ >> z_ >> _r >> _g >> _b) 
  {
	  pcl::PointXYZRGB pt;
	  pt.x = x_;
	  pt.y = y_;
	  pt.z = z_;
	  pt.r = _r;
	  pt.g = _g;
	  pt.b = _b;
	  cloud->points.push_back(pt);
  }
  vtkObject::GlobalWarningDisplayOff();
  vizualizeMesh2(cloud);  
  return 0;
}