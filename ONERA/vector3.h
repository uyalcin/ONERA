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

    private:
        float x;
        float y;
        float z;
};

#endif // VECTOR3_H
