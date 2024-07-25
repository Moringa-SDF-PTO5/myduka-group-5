import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const ItemsTable = ({ items }) => (
  <TableContainer component={Paper}>
    <Table>
      <TableHead>
        <TableRow>
          <TableCell>Item Name</TableCell>
          <TableCell>Quantity</TableCell>
          <TableCell>Payment Status</TableCell>
          <TableCell>Buying Price</TableCell>
          <TableCell>Selling Price</TableCell>
          <TableCell>Items Spoilt</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {items.map((item, index) => (
          <TableRow key={index}>
            <TableCell>{item.itemName}</TableCell>
            <TableCell>{item.quantity}</TableCell>
            <TableCell>{item.paymentStatus}</TableCell>
            <TableCell>{item.buyingPrice}</TableCell>
            <TableCell>{item.sellingPrice}</TableCell>
            <TableCell>{item.itemsSpoilt}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  </TableContainer>
);

export default ItemsTable;
