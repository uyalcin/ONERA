#include "vector3.h"

Vector3::Vector3() :
    x(0),
    y(0),
    z(0)
{
}

Vector3::Vector3(float _x, float _y, float _z) :
    x(_x),
    y(_y),
    z(_z)
{
}

Vector3::~Vector3()
{

}

float Vector3::getX()
{
    return x;
}

float Vector3::getY()
{
    return y;
}

float Vector3::getZ()
{
    return z;
}

std::ostream& operator<<(std::ostream& out, const Vector3 &v)
{
    out << "(" << v.x
       << ", " << v.y
       << ", " << v.z
       << ")";
    return out;
}
