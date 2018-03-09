#ifndef BOX_H
#define BOX_H

#include <vector>

class Box
{
public:
    Box();
private:
    Vector3<float> dimension;
    Vector3<float> position;
};

#endif // BOX_H
