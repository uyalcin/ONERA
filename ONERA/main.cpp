#include "mainwindow.h"
#include "renderwindow.h"
#include <QApplication>
#include <GL/glut.h>
#include <QtGui/QApplication>

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();
}
