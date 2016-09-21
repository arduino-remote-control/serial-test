#include <Python.h>
#include <stdio.h>

typedef struct {
    char cmd;
    int number;
} command;

static PyObject* to_class(PyObject* self, PyObject* args)
{
    char *data;
    if (!PyArg_ParseTuple(args, "s#", &data)) {
        return NULL;
    }

    command cmd;
    int size = sizeof(data);
    memcpy(&cmd, data, size);

    return Py_BuildValue("ci", cmd.cmd, cmd.number);
}

static PyMethodDef structConvert[] =
{
     {"to_class", to_class, METH_VARARGS, "convert char* to class"},
     {NULL, NULL, 0, NULL}
};

static struct PyModuleDef sc_module =
{
    PyModuleDef_HEAD_INIT,
    "sc_module",
    "",
    -1,
    structConvert
};

/* module initialization */
PyMODINIT_FUNC PyInit_sc_module(void)
{
    return PyModule_Create(&sc_module);
}
