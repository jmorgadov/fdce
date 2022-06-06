#define PY_SSIZE_T_CLEAN
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>

double d_1, d_2, c1, c2, c3;
int n, m, v, m_min;
int N, M;

#define GET1(arr, i) *((double *)PyArray_GETPTR1(arr, i))
#define GET3(arr, i, j, k) *((double *)PyArray_GETPTR3(arr, i, j, k))
#define SET3(arr, i, j, k, val) PyArray_SETITEM(arr, PyArray_GETPTR3(arr, i, j, k), PyFloat_FromDouble(val))

#define MIN(a, b) (a < b ? a : b)

PyArrayObject* _get_coeff(float x_0, PyArrayObject* a, int ord, PyArrayObject* coeff_arr){
	N = PyArray_DIM(a, 0);
	M = ord + 1;
	SET3(coeff_arr, 0, 0, 0, 1);

	c1 = 1;
	for (n = 1; n < N; n++){
		c2 = 1;
		m_min = MIN(n + 1, M);
		for (v = 0; v< n; v++){
			c3 = GET1(a, n) - GET1(a, v);
			c2 = c2 * c3;
			if (n < M) SET3(coeff_arr, n, n - 1, v, 0);
			for (m = 0; m < m_min; m++){
				d_1 = GET3(coeff_arr, m, n -1, v);
				d_2 = m == 0 ? 0 : GET3(coeff_arr, m - 1, n - 1, v);
				SET3(coeff_arr, m, n, v, ((GET1(a, n) - x_0) * d_1 - m * d_2) / c3);
			}
		}
		for (m = 0; m < m_min; m++){
			d_1 = m == 0? 0 : GET3(coeff_arr, m - 1, n - 1, n - 1);
			d_2 = GET3(coeff_arr, m, n - 1, n - 1);
			SET3(coeff_arr, m, n, n, (c1 / c2) * (m * d_1 - (GET1(a, n - 1) - x_0) * d_2));
		}
		c1 = c2;
	}
	return coeff_arr;
}

PyObject* get_coeff(PyObject* self, PyObject* args, PyObject* keywds){
	PyObject *a;
	PyObject *coeff_arr = NULL;
	float x_0;
	int ord = 1;

	static char *kwlist[] = { "x_0", "a", "M", "coeff_arr", NULL };

	if (!PyArg_ParseTupleAndKeywords(args, keywds, "dO!|iO!", kwlist, &x_0, &PyArray_Type, &a, &ord, &PyArray_Type, &coeff_arr))
		return NULL;

	a = PyArray_FROM_OTF(a, NPY_DOUBLE, NPY_ARRAY_IN_ARRAY);

	if (coeff_arr == NULL){
		// Create a new coeff_arr if not provided
		int a_len = PyArray_DIM((PyArrayObject*)a, 0);
		npy_intp dims[] = {ord + 1, a_len, a_len};
		coeff_arr = PyArray_SimpleNew(3, dims, NPY_DOUBLE);
	}
	else {
		coeff_arr = PyArray_FROM_OTF(coeff_arr, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY);
	}

	_get_coeff(x_0, (PyArrayObject*)a, ord, (PyArrayObject*)coeff_arr);
	return PyArray_Return((PyArrayObject*)coeff_arr);
}


static PyMethodDef _fdce_methods[] = {
	{"get_coeff", (PyCFunction)get_coeff, METH_VARARGS | METH_KEYWORDS, "Get coefficients"},
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef _fdce_module = {
	PyModuleDef_HEAD_INIT,
	"_fdce",
	NULL,
	-1,
	_fdce_methods
};

PyMODINIT_FUNC PyInit__fdce(void){
	PyObject *m = PyModule_Create(&_fdce_module);
	if (m == NULL)
		return NULL;
	import_array();
	return m;
}
