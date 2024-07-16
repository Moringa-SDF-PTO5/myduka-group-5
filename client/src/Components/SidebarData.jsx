import React from 'react'
import DashboardIcon from '@mui/icons-material/Dashboard';
import CategoryIcon from '@mui/icons-material/Category';
import InventoryIcon from '@mui/icons-material/Inventory';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import GroupsIcon from '@mui/icons-material/Groups';
import ManageAccountsIcon from '@mui/icons-material/ManageAccounts';
import StoreIcon from '@mui/icons-material/Store';
import LogoutIcon from '@mui/icons-material/Logout';

export const SidebarData = [
    {
        title: 'Dashboard',
        icon: <DashboardIcon />,
        link:'/dashboard'
    },
    {
        title: 'Category',
        icon: <CategoryIcon />,
        link:'/category'
    },
    {
        title: 'Products',
        icon: <CheckCircleIcon />,
        link:'/products'
    },
    {
        title: 'Orders',
        icon: <InventoryIcon />,
        link:'/orders'
    },
    {
        title: 'Members',
        icon: <GroupsIcon />,
        link:'/members'
    },
    {
        title: 'Permission',
        icon: <ManageAccountsIcon />,
        link:'/permission'
    },
    {
        title: 'Store',
        icon: <StoreIcon />,
        link:'/store'
    },
    {
        title: 'Logout',
        icon: <LogoutIcon />,
        link:'/logout'
    }



]