/* eslint-disable react/prop-types */
import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Button, TextField, FormControl, InputLabel, Select, MenuItem } from '@mui/material';

const validationSchema = Yup.object({
  itemName: Yup.string().required('Item Name is required'),
  quantity: Yup.number().required('Quantity is required'),
  paymentStatus: Yup.string().required('Payment Status is required'),
  buyingPrice: Yup.number().required('Buying Price is required'),
  sellingPrice: Yup.number().required('Selling Price is required'),
  itemsSpoilt: Yup.number().required('Number of items spoilt is required'),
});

const ItemForm = ({ onSubmit }) => {
  const formik = useFormik({
    initialValues: {
      itemName: '',
      quantity: '',
      paymentStatus: '',
      buyingPrice: '',
      sellingPrice: '',
      itemsSpoilt: '',
    },
    validationSchema,
    onSubmit,
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <TextField
        fullWidth
        id="itemName"
        name="itemName"
        label="Item Name"
        value={formik.values.itemName}
        onChange={formik.handleChange}
        error={formik.touched.itemName && Boolean(formik.errors.itemName)}
        helperText={formik.touched.itemName && formik.errors.itemName}
        margin="normal"
      />
      <TextField
        fullWidth
        id="quantity"
        name="quantity"
        label="Quantity"
        type="number"
        value={formik.values.quantity}
        onChange={formik.handleChange}
        error={formik.touched.quantity && Boolean(formik.errors.quantity)}
        helperText={formik.touched.quantity && formik.errors.quantity}
        margin="normal"
      />
      <FormControl fullWidth margin="normal">
        <InputLabel id="paymentStatus-label">Payment Status</InputLabel>
        <Select
          labelId="paymentStatus-label"
          id="paymentStatus"
          name="paymentStatus"
          value={formik.values.paymentStatus}
          onChange={formik.handleChange}
          error={formik.touched.paymentStatus && Boolean(formik.errors.paymentStatus)}
        >
          <MenuItem value="paid">Paid</MenuItem>
          <MenuItem value="not paid">Not Paid</MenuItem>
        </Select>
      </FormControl>
      <TextField
        fullWidth
        id="buyingPrice"
        name="buyingPrice"
        label="Buying Price"
        type="number"
        value={formik.values.buyingPrice}
        onChange={formik.handleChange}
        error={formik.touched.buyingPrice && Boolean(formik.errors.buyingPrice)}
        helperText={formik.touched.buyingPrice && formik.errors.buyingPrice}
        margin="normal"
      />
      <TextField
        fullWidth
        id="sellingPrice"
        name="sellingPrice"
        label="Selling Price"
        type="number"
        value={formik.values.sellingPrice}
        onChange={formik.handleChange}
        error={formik.touched.sellingPrice && Boolean(formik.errors.sellingPrice)}
        helperText={formik.touched.sellingPrice && formik.errors.sellingPrice}
        margin="normal"
      />
      <TextField
        fullWidth
        id="itemsSpoilt"
        name="itemsSpoilt"
        label="Items Spoilt"
        type="number"
        value={formik.values.itemsSpoilt}
        onChange={formik.handleChange}
        error={formik.touched.itemsSpoilt && Boolean(formik.errors.itemsSpoilt)}
        helperText={formik.touched.itemsSpoilt && formik.errors.itemsSpoilt}
        margin="normal"
      />
      <Button color="primary" variant="contained" fullWidth type="submit">
        Add Item
      </Button>
    </form>
  );
};

export default ItemForm;
