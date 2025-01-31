import React from 'react'
import DashboardIcon from '@mui/icons-material/Dashboard';
// import CategoryIcon from '@mui/icons-material/Category';
import InventoryIcon from '@mui/icons-material/Inventory';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import GroupsIcon from '@mui/icons-material/Groups';
import StoreIcon from '@mui/icons-material/Store';
// import LogoutIcon from '@mui/icons-material/Logout';

export const sidebarNav = [
    {
        title: 'Dashboard',
        icon: <DashboardIcon />,
        link:'/dashboard',
        allowedRoles: ['admin','clerk','merchant']
    },
    {
        title: 'Products',
        icon: <CheckCircleIcon />,
        link:'/products',
        allowedRoles: ['admin','clerk','merchant']
    },
    {
        title: 'Orders',
        icon: <InventoryIcon />,
        link:'/orders',
        allowedRoles: ['admin','clerk','merchant']
    },
    {
        title: 'Users',
        icon: <GroupsIcon />,
        link:'/users',
        allowedRoles: ['admin']
    },
    {
        title: 'Stores',
        icon: <StoreIcon />,
        link:'/stores',
        allowedRoles: ['admin']
    },
    // {
    //     title: 'Logout',
    //     icon: <LogoutIcon />,
    //     link:'/logout',
    //     allowedRoles: ['admin','clerk','merchant']
    // }



]