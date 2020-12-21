#include <iostream>
#include <pcl/point_types.h>
#include <pcl/filters/radius_outlier_removal.h>
#include <pcl/filters/conditional_removal.h>
#include <string>
#include <iostream>
#include <fstream>

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

int main(int argc, char** argv)
{
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>);
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_filtered(new pcl::PointCloud<pcl::PointXYZ>);
	std::vector<std::string> vecOfStr;
	std::ofstream outfile;

	std::string name_input_file = (argc > 0) ? argv[0] : "cloud_voxel.xyz";
	bool result = getFileContent(name_input_file, vecOfStr);
	std::string name_out_file = (argc > 1) ? argv[1] : "cloud_smot.xyz";
	float radius_length = (argc > 2) ? stof(argv[2]) : 0.18;
	int number_of_neighbors = (argc > 3) ? stoi(argv[3]) : 5;

	if (remove(name_out_file.c_str()) != 0)
		perror("Error deleting file");
	else
		puts("File successfully deleted");
	outfile.open(name_out_file, std::ios_base::app);

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
	cloud->points.resize(linee.size());
	for (std::size_t i = 0; i < linee.size() - 2; ++i)
	{
		cloud->points[i].x = stof(pom[3 * i]);
		cloud->points[i].y = stof(pom[3 * i + 1]);
		cloud->points[i].z = stof(pom[3 * i + 2]);
	}
	std::cout << "cloud before filtering" << std::endl;
	std::cout << (cloud->points.size()) << std::endl;
	pcl::RadiusOutlierRemoval<pcl::PointXYZ> outrem;
	// build the filter
	outrem.setInputCloud(cloud);
	outrem.setRadiusSearch(radius_length);
	outrem.setMinNeighborsInRadius(number_of_neighbors);
	// apply filter
	outrem.filter(*cloud_filtered);
	// display pointcloud after filtering
	std::cerr << "Cloud size after filtering: " << std::endl;
	std::cout << cloud_filtered->points.size() << std::endl;
	for (std::size_t i = 0; i < cloud_filtered->points.size(); ++i)
		outfile << cloud_filtered->points[i].x << " "
		<< cloud_filtered->points[i].y << " "
		<< cloud_filtered->points[i].z << std::endl;
	double pr = 100 - ((double(cloud_filtered->points.size()) / double(cloud->points.size())) * 100);
	std::cout << "procentage remove " << pr << std::endl;
	outfile.close();
	return (0);
}