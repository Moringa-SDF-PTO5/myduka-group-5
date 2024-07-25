// Dashboard.js
import React, { useState } from 'react';
import { Container, Grid, Typography, Button } from '@mui/material';
import SummaryPage from '../records/summaryPage';
import ItemForm from '../records/itemForm';
import ItemsTable from '../records/itemsTable';

const RecordsPage = () => {
  const [items, setItems] = useState([]);
  
  const handleAddItem = (newItem) => {
    setItems([...items, newItem]);
  };

  const totalItems = items.reduce((sum, item) => sum + item.quantity, 0);
  const totalSpoiltItems = items.reduce((sum, item) => sum + item.itemsSpoilt, 0);
  const totalPaidItems = items.filter(item => item.paymentStatus === 'paid').length;
  const totalUnpaidItems = items.filter(item => item.paymentStatus === 'not paid').length;

  return (
    <Container maxWidth="lg">
      <Typography variant="h4" component="h1" gutterBottom>
        Records Dashboard
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={3}>
          <SummaryPage title="Total Items" value={totalItems} />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <SummaryPage title="Total Spoilt Items" value={totalSpoiltItems} />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <SummaryPage title="Total Paid Items" value={totalPaidItems} />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <SummaryPage title="Total Unpaid Items" value={totalUnpaidItems} />
        </Grid>
        <Grid item xs={12}>
          <ItemForm onSubmit={handleAddItem} />
        </Grid>
        <Grid item xs={12}>
          <ItemsTable items={items} />
        </Grid>
        <Grid item xs={12}>
          <Button color="secondary" variant="contained" fullWidth>
            Request More Supply
          </Button>
        </Grid>
      </Grid>
    </Container>
  );
};

export default RecordsPage;

