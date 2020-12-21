#include <iostream>
#include <string>
#include <fstream>
#include <pcl/point_types.h>
#include <pcl/filters/passthrough.h>
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
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>), cloud_filtered_blob(new pcl::PointCloud<pcl::PointXYZ>);
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_filtered(new pcl::PointCloud<pcl::PointXYZ>); //x
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_filtered1(new pcl::PointCloud<pcl::PointXYZ>); //y
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_filtered2(new pcl::PointCloud<pcl::PointXYZ>); // z
	std::vector<std::string> vecOfStr;
	std::ofstream outfile;
	std::string name_input_file = (argc > 1) ? argv[1] : "cloud_voxel.xyz";
	bool result = getFileContent(name_input_file, vecOfStr);
	std::string name_out_file = (argc > 2) ? argv[2] : "cloud_trou.xyz";
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
	std::string x_min = (argc > 3) ? argv[3] : "-0.4";
	std::string x_max = (argc > 4) ? argv[4] : "0.4";
	std::string y_min = (argc > 5) ? argv[5] : "-0.2";
	std::string y_max = (argc > 6) ? argv[6] : "0.4";
	std::string z_min = (argc > 7) ? argv[7] : "-0.2";
	std::string z_max = (argc > 8) ? argv[8] : "0.4";
	// axis x
	pcl::PassThrough<pcl::PointXYZ> pass;
	pass.setInputCloud(cloud);
	pass.setFilterFieldName("x");
	pass.setFilterLimits(std::stof(x_min), std::stof(x_max));
	pass.filter(*cloud_filtered);
	// axis y
	pcl::PassThrough<pcl::PointXYZ> pass1;
	pass1.setInputCloud(cloud_filtered);
	pass1.setFilterFieldName("y");
	pass1.setFilterLimits(std::stof(y_min), std::stof(y_max));
	pass1.filter(*cloud_filtered1);
	// axis z
	pcl::PassThrough<pcl::PointXYZ> pass2;
	pass2.setInputCloud(cloud_filtered1);
	pass2.setFilterFieldName("z");
	pass2.setFilterLimits(std::stof(z_min), std::stof(z_max));
	pass2.filter(*cloud_filtered2);
	
	if (remove(name_out_file.c_str()) != 0)
		perror("Error deleting file");
	else
		puts("File successfully deleted");
	outfile.open(name_out_file, std::ios_base::app);
	for (int i = 0; i < cloud_filtered2->size(); i++)
	{
		if (cloud_filtered2->points[i].x!=0.0 && cloud_filtered2->points[i].y!=0.0 && cloud_filtered2->points[i].z!=0.0)
			outfile << cloud_filtered2->points[i].x << " "
				<< cloud_filtered2->points[i].y << " "
				<< cloud_filtered2->points[i].z << std::endl;
	}
	outfile.close();
	return (0);
}