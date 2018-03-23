#ifndef BOX_H
#define BOX_H

#include "vector3.h"

class Box
{
public:
    Box(Vector3 _dimension);
    Vector3 getPosition();
    Vector3 getDimension();
    void setPosition(Vector3 _position);
private:
<<<<<<< HEAD

=======
    Vector3 dimension;
    Vector3 position;
>>>>>>> model
};

#endif // BOX_H
