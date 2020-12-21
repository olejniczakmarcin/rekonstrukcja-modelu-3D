#include <iostream>
#include <string>
#include <fstream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/voxel_grid.h>
using namespace std;

vector<string> split(string s, string delimiter) {
	size_t pos_start = 0, pos_end, delim_len = delimiter.length();
	string token;
	vector<string> res;

	while ((pos_end = s.find(delimiter, pos_start)) != string::npos) {
		token = s.substr(pos_start, pos_end - pos_start);
		pos_start = pos_end + delim_len;
		res.push_back(token);
	}

	res.push_back(s.substr(pos_start));
	return res;
}
bool getFileContent(std::string fileName, std::vector<std::string> & vecOfStrs)
{
	// Open the File
	std::ifstream in(fileName.c_str());
	if (!in)
	{
		std::cerr << "Cannot open the File : " << fileName << std::endl;
		return false;
	}
	std::string str;
	while (std::getline(in, str))
	{
		if (str.size() > 0)
			vecOfStrs.push_back(str);
	}
	in.close();
	return true;
}

int
main(int argc, char** argv)
{
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>);
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_filtered(new pcl::PointCloud<pcl::PointXYZ>);
	std::vector<std::string> vecOfStr;
	std::ofstream outfile;
	std::string name_input_file = (argc > 1) ? argv[1] : "smo_c.xyz";
	bool result = getFileContent(name_input_file, vecOfStr);
	std::string name_out_file = (argc > 2) ? argv[2] : "cloud_voxel.xyz";
	float side_length = (argc > 3) ? atof(argv[3]) : 0.018;
	int len = vecOfStr.size();
	string table;
	vector<string> linee;
	if (result)
	{
		for (std::string & line : vecOfStr)
		{
			linee.push_back(line);
		}
	}
	string delimiter = " ";
	vector<string> pom;
	for (int i = 0; i < linee.size(); i++)
	{
		vector<string> v = split(linee[i], delimiter);
		for (int j = 0; j < v.size(); j++)
		{
			pom.push_back(v[j]);
		}
	}

	// Fill in the cloud data //default value
	//cloud->width  = 5;
	//cloud->height = 1;
	cloud->points.resize(linee.size());

	for (std::size_t i = 0; i < linee.size() - 2; ++i)
	{
		cloud->points[i].x = stof(pom[3 * i]);
		cloud->points[i].y = stof(pom[3 * i + 1]);
		cloud->points[i].z = stof(pom[3 * i + 2]);
	}
	std::cout << "cloud before filtering" << std::endl;
	std::cout << (cloud->points.size()) << std::endl;

	pcl::VoxelGrid<pcl::PointXYZ> sor;
	sor.setInputCloud(cloud);
	sor.setLeafSize(side_length, side_length, side_length);  //(0.01f, 0.01f, 0.01f) default value
	sor.filter(*cloud_filtered);

	std::cerr << "PointCloud after filtering: " << cloud_filtered->width * cloud_filtered->height
		<< " data points (" << pcl::getFieldsList(*cloud_filtered) << ").";

	if (remove(name_out_file.c_str()) != 0)
		perror("Error deleting file");
	else
		puts("File successfully deleted");
	outfile.open(name_out_file, std::ios_base::app);//std::ios_base::app
	for (int i = 0; i < cloud_filtered->size(); i++)
	{
		if(cloud_filtered->points[i].x!=0 && cloud_filtered->points[i].y!=0 && cloud_filtered->points[i].z!=0)
			outfile << cloud_filtered->points[i].x << " "
				<< cloud_filtered->points[i].y << " "
				<< cloud_filtered->points[i].z << std::endl;
	}
	outfile.close();
	return (0);
}