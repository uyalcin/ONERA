#include <iostream>

#ifndef VECTOR3_H
#define VECTOR3_H


class Vector3
{
    public:
        Vector3();
        Vector3(float _x, float _y, float _z);
        ~Vector3();

        float getX();
        float getY();
        float getZ();

        friend std::ostream& operator<<(std::ostream& out, const Vector3 &v);

    private:
        float x;
        float y;
        float z;
};

#endif // VECTOR3_H
